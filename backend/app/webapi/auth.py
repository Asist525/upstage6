import os
import uuid
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from app.core.settings import get_settings
from app.core.db import get_session, User
from app.core.auth import create_access_token, get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

router = APIRouter()

def get_google_oauth():
    settings = get_settings()
    
    # [CRITICAL FIX] Pydantic이 못 읽을 경우를 대비해 직접 OS 환경 변수 확인
    client_id = settings.google_client_id or os.getenv("GOOGLE_CLIENT_ID")
    client_secret = settings.google_client_secret or os.getenv("GOOGLE_CLIENT_SECRET")
    
    if not client_id:
        print("CRITICAL ERROR: GOOGLE_CLIENT_ID is still None!")
    
    _oauth = OAuth()
    _oauth.register(
        name='google',
        client_id=client_id,
        client_secret=client_secret,
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    return _oauth.google

@router.get("/login")
async def login(request: Request):
    google = get_google_oauth()
    
    # redirect_uri를 생성
    redirect_uri = request.url_for('auth_callback')
    
    # Cloudflare 환경(daehak.cc)에서는 https가 필수이지만, 
    # 로컬(localhost) 개발 시에는 http를 유지해야 함.
    host = request.headers.get("host", "")
    if "localhost" not in host and "127.0.0.1" not in host:
        redirect_uri = str(redirect_uri).replace("http://", "https://")
    else:
        redirect_uri = str(redirect_uri)
    
    print(f"DEBUG: Using redirect_uri: {redirect_uri}")
    return await google.authorize_redirect(request, redirect_uri)

@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request, session: AsyncSession = Depends(get_session)):
    import logging
    logger = logging.getLogger("app.auth")
    google = get_google_oauth()
    try:
        logger.info("Starting OAuth callback processing")
        token = await google.authorize_access_token(request)
        logger.info("OAuth token received successfully")
    except Exception as e:
        logger.exception("OAuth authorization failed at token exchange")
        raise HTTPException(status_code=400, detail=f"OAuth authorization failed: {str(e)}")
        
    user_info = token.get('userinfo')
    if not user_info:
        logger.error("Failed to get userinfo from token")
        raise HTTPException(status_code=400, detail="Failed to get user info from Google")

    email = user_info.get('email')
    name = user_info.get('name')
    picture = user_info.get('picture')
    logger.info(f"Processing login for user: {email}")

    try:
        async with session as s:
            # Check if user exists
            result = await s.execute(select(User).where(User.email == email))
            user = result.scalar_one_or_none()

            if not user:
                logger.info(f"Creating new user in DB: {email}")
                # Create new user
                user = User(
                    id=str(uuid.uuid4()),
                    email=email,
                    name=name,
                    picture=picture
                )
                s.add(user)
                await s.commit()
                await s.refresh(user)
            else:
                logger.info(f"Existing user found: {email}")
    except Exception as e:
        logger.exception("Database operation failed during user login/creation")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    try:
        # Generate JWT
        access_token = create_access_token(data={"sub": user.id})
        logger.info("JWT token generated successfully")
        
        # Redirect to frontend with token
        settings = get_settings()
        frontend_url = f"{settings.frontend_origin}?token={access_token}"
        logger.info(f"Redirecting to frontend: {frontend_url}")
        return RedirectResponse(url=frontend_url)
    except Exception as e:
        logger.exception("JWT generation or redirection failed")
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {
        "id": current_user.id,
        "email": current_user.email,
        "name": current_user.name,
        "picture": current_user.picture
    }
