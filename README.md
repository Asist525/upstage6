제공해주신 내용을 바탕으로, GitHub 포트폴리오용 README.md로서의 가독성과 전문성을 높이는 방향으로 정리했습니다.주요 변경 사항:가독성 강화: 이모지 활용, 계층 구조 명확화, 중요 키워드 강조.기여도(Contribution) 섹션 강조: 포트폴리오 목적에 맞게 본인의 기여 부분을 명확히 구분하고, 시각적으로 돋보이게 배치했습니다.설치 및 실행 가이드 정리: 코드 블록을 분리하여 복사-붙여넣기가 쉽도록 정돈했습니다.아래 내용을 복사하여 README.md 파일에 바로 사용하시면 됩니다.🖋️ TEAM CONTEXTOR원고 분석을 위한 지능형 멀티 에이전트 시스템 (Intelligent Multi-Agent System for Manuscript Analysis) > 사용자가 업로드한 원고(PDF/DOCX/TXT/MD)를 분석하여 가독성, 톤, 인과관계, 부적절한 표현 등을 진단하고, 종합적인 전문가 리포트를 제공합니다.👤 Maintainer Info (Portfolio Fork)Maintainer: 박건원 (GitHub: Asist525)Role: Frontend Lead / UI·UX Optimization / Feature ImplementationContext: 본 레포지토리는 TEAM CONTEXTOR (TEAM SIX) 해커톤 프로젝트를 기반으로, 개인 포트폴리오 및 기술 데모 목적으로 포크(Fork)하여 관리하는 버전입니다.🏆 My Verified Contributions핵심 기여 사항팀 프로젝트 중 제가 주도적으로 개발하고 기여한 핵심 기능과 커밋 내역입니다.Evidence: Commits by Asist5251. UI/UX & Visualization (Frontend Lead)사용자가 분석 결과를 직관적으로 이해할 수 있도록 시각화 및 인터랙션 로직을 전담하여 구현했습니다.Highlight System (협업 기능 구현)이슈가 발생한 텍스트 구간(Span)을 계산하여 원문에 형광펜 효과 적용이슈 타입별(가독성, 혐오 표현 등) 색상 팔레트 시스템 구축 및 가시성 강화Hover 시 상세 분석 내용을 보여주는 커스텀 툴팁(Tooltip) 컴포넌트 개발Persona Settings UI독자 페르소나/관점 설정을 위한 제어 패널 UI 구현복잡한 설정 로직을 사용자 친화적인 워크플로우로 정리2. Key Commits (Code Level)면접 및 코드 리뷰 시 참고할 수 있는 주요 커밋 내역입니다.TypeCommit MessageHashDescriptionFeatResponsive UI + Tooltip + Highlight UX3cb9120반응형 레이아웃 및 하이라이트/툴팁 핵심 로직 구현StyleHighlight Color Palette8682d57이슈 심각도 및 카테고리에 따른 색상 구분성 강화FixHighlight Rendering Fixf6167dc텍스트 오프셋 매핑 오류 수정 및 렌더링 최적화RefactorPersona UI & Settings3842878페르소나 설정 상태 관리 및 UI 컴포넌트 구조 개선🚀 Key Features (Project Overview)1. 다양한 문서 지원 & 강력한 파싱Upstage Document Parse 연동: PDF, DOCX, HWP, HWPX, TXT, MD 등 다양한 포맷 지원.Robust Local Fallback: 외부 API 실패 시 내장 파서(HWP Record Parsing, XML Parsing 등)로 자동 전환하여 안정성 확보.2. 지능형 멀티 에이전트 파이프라인 (Multi-Agent Pipeline)각 분야의 전문가 역할을 하는 AI 에이전트들이 유기적으로 협업합니다.🕵️ Narrative Analyst: 인과관계, 전개 흐름, 긴장도(Tension) 분석.🎨 Tone & Style Expert: 문체 일관성, 가독성, 어조 평가.🛡️ Safety Guard: 트라우마 유발 요소, 혐오/차별 표현 탐지.🎭 Genre Specialist: 장르적 클리셰 분석 및 독창성 평가.3. 신뢰성 검증 시스템 (Self-Evaluation)LLM-as-a-Judge: 별도의 평가 에이전트가 각 분석 결과의 타당성을 교차 검증하여 QA Score 산출.Real-time Feedback: 분석 직후 대시보드에서 각 에이전트의 성능/신뢰도 점수 확인 가능.4. Chief Editor's Report분산된 에이전트들의 분석 결과를 종합하여, 편집장이 작성한 듯한 단일 Markdown 리포트로 제공.🛠 Tech StackBackendCategoryTechnologyFrameworkFastAPI (Python 3.11+)LLMUpstage Solar (solar-pro2)OrchestrationLangChain / Custom Agent LogicDatabaseSQLite (SQLAlchemy)ParsingUpstage Document Parse, python-docx, pypdfObservabilityLangSmithFrontendCategoryTechnologyFrameworkReact 18 (Vite)Renderingreact-markdown, Custom Highlight logicStylingTailwind CSS (Predicted) / Styled Components💻 Getting Started1. PrerequisitesPython 3.11+Node.js 18+2. Backend SetupBashcd backend

# 가상환경 생성 및 활성화
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 의존성 설치
pip install -e .

# 환경변수 설정
cp .env.example .env
# .env 파일을 열어 UPSTAGE_API_KEY 등을 입력하세요.

# (선택) DB 마이그레이션
# backend/data/team.db에 스키마 변경 사항이 있을 경우 실행
python backend/migrations/apply_sqlite_migrations.py

# 서버 실행
uvicorn main:app --port 8000
3. Frontend SetupBashcd frontend

# 패키지 설치
npm install
npm install docx

# 개발 서버 실행
npm run dev
App URL: http://localhost:5173API Docs: http://localhost:8000/docs📂 Project Structureupstage6/
├── backend/
│   ├── app/
│   │   ├── agents/      # 지능형 에이전트 로직 (Tone, Causality, Report 등)
│   │   ├── api/         # FastAPI 라우터 및 엔드포인트
│   │   ├── core/        # DB 설정, Config 관리
│   │   └── services/    # 파이프라인 오케스트레이션 서비스
│   └── data/            # SQLite DB 및 업로드 파일 저장소
├── frontend/
│   ├── src/
│   │   ├── api.js       # Axios 기반 백엔드 통신 레이어
│   │   └── App.jsx      # 메인 UI, 결과 뷰어, 하이라이트 로직
│   └── public/
└── README.md
🔌 API OverviewMethodEndpointDescriptionPOST/api/documents/upload문서 업로드 및 텍스트 추출GET/api/documents업로드된 문서 목록 조회POST/api/analysis/run/{id}멀티 에이전트 분석 파이프라인 실행GET/api/analysis/{id}최종 리포트 및 상세 데이터(하이라이트 정보) 조회📜 LicenseThis project is developed for the Upstage AI Lab program.
