우측 상단의 **복사 버튼**을 누르면 전체 내용을 한 번에 가져가실 수 있습니다.

```markdown
# 🖋️ TEAM CONTEXTOR

> **원고 분석을 위한 지능형 멀티 에이전트 시스템 (Intelligent Multi-Agent System for Manuscript Analysis)**
> 사용자가 업로드한 원고(PDF/DOCX/TXT/MD)를 분석하여 가독성, 톤, 인과관계, 부적절한 표현 등을 진단하고, 종합적인 전문가 리포트를 제공합니다.

---

## 👤 Maintainer Info (Portfolio Fork)

- **Maintainer**: 박건원 (GitHub: [Asist525](https://github.com/Asist525))
- **Role**: Frontend Lead / UI·UX Optimization / Feature Implementation
- **Context**: 본 레포지토리는 **TEAM CONTEXTOR (TEAM SIX)** 해커톤 프로젝트를 기반으로, **개인 포트폴리오 및 기술 데모 목적**으로 포크(Fork)하여 관리하는 버전입니다.

---

## 🏆 My Verified Contributions

> **핵심 기여 사항**
> 팀 프로젝트 중 제가 주도적으로 개발하고 기여한 핵심 기능과 커밋 내역입니다.  
> Evidence: [Commits by Asist525](commits/main?author=Asist525)

### 1. UI/UX & Visualization (Frontend Lead)
사용자가 분석 결과를 직관적으로 이해할 수 있도록 시각화 및 인터랙션 로직을 전담하여 구현했습니다.

* **Highlight System (협업 기능 구현)**
    * 이슈가 발생한 텍스트 구간(Span)을 계산하여 원문에 **형광펜 효과** 적용
    * 이슈 타입별(가독성, 혐오 표현 등) 색상 팔레트 시스템 구축 및 가시성 강화
    * Hover 시 상세 분석 내용을 보여주는 **커스텀 툴팁(Tooltip)** 컴포넌트 개발
* **Persona Settings UI**
    * 독자 페르소나/관점 설정을 위한 제어 패널 UI 구현
    * 복잡한 설정 로직을 사용자 친화적인 워크플로우로 정리

### 2. Key Commits (Code Level)
면접 및 코드 리뷰 시 참고할 수 있는 주요 커밋 내역입니다.

| Type | Commit Message | Hash | Description |
| :--- | :--- | :--- | :--- |
| **Feat** | Responsive UI + Tooltip + Highlight UX | [`3cb9120`](commit/3cb9120a748017626b95c0f900229e8fcf4ad29c) | 반응형 레이아웃 및 하이라이트/툴팁 핵심 로직 구현 |
| **Style** | Highlight Color Palette | [`8682d57`](commit/8682d57cf63a2982d8c22cf3881e5c268e2397fd) | 이슈 심각도 및 카테고리에 따른 색상 구분성 강화 |
| **Fix** | Highlight Rendering Fix | [`f6167dc`](commit/f6167dc5292a7e8a3bba0cb644f5b92ca1bd9cc5) | 텍스트 오프셋 매핑 오류 수정 및 렌더링 최적화 |
| **Refactor**| Persona UI & Settings | [`3842878`](commit/384287896656e700a13425e6362e09c44e38c7e4) | 페르소나 설정 상태 관리 및 UI 컴포넌트 구조 개선 |

---

## 🚀 Key Features (Project Overview)

### 1. 다양한 문서 지원 & 강력한 파싱
* **Upstage Document Parse 연동**: PDF, DOCX, HWP, HWPX, TXT, MD 등 다양한 포맷 지원.
* **Robust Local Fallback**: 외부 API 실패 시 내장 파서(HWP Record Parsing, XML Parsing 등)로 자동 전환하여 안정성 확보.

### 2. 지능형 멀티 에이전트 파이프라인 (Multi-Agent Pipeline)
각 분야의 전문가 역할을 하는 AI 에이전트들이 유기적으로 협업합니다.
* **🕵️ Narrative Analyst**: 인과관계, 전개 흐름, 긴장도(Tension) 분석.
* **🎨 Tone & Style Expert**: 문체 일관성, 가독성, 어조 평가.
* **🛡️ Safety Guard**: 트라우마 유발 요소, 혐오/차별 표현 탐지.
* **🎭 Genre Specialist**: 장르적 클리셰 분석 및 독창성 평가.

### 3. 신뢰성 검증 시스템 (Self-Evaluation)
* **LLM-as-a-Judge**: 별도의 평가 에이전트가 각 분석 결과의 타당성을 교차 검증하여 QA Score 산출.
* **Real-time Feedback**: 분석 직후 대시보드에서 각 에이전트의 성능/신뢰도 점수 확인 가능.

### 4. Chief Editor's Report
* 분산된 에이전트들의 분석 결과를 종합하여, 편집장이 작성한 듯한 **단일 Markdown 리포트**로 제공.

---

## 🛠 Tech Stack

### Backend
| Category | Technology |
| :--- | :--- |
| **Framework** | FastAPI (Python 3.11+) |
| **LLM** | Upstage Solar (solar-pro2) |
| **Orchestration** | LangChain / Custom Agent Logic |
| **Database** | SQLite (SQLAlchemy) |
| **Parsing** | Upstage Document Parse, python-docx, pypdf |
| **Observability**| LangSmith |

### Frontend
| Category | Technology |
| :--- | :--- |
| **Framework** | React 18 (Vite) |
| **Rendering** | react-markdown, Custom Highlight logic |
| **Styling** | Tailwind CSS (Predicted) / Styled Components |

---

## 💻 Getting Started

### 1. Prerequisites
* Python 3.11+
* Node.js 18+

### 2. Backend Setup
```bash
cd backend

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

```

### 3. Frontend Setup

```bash
cd frontend

# 패키지 설치
npm install
npm install docx

# 개발 서버 실행
npm run dev

```

* **App URL**: `http://localhost:5173`
* **API Docs**: `http://localhost:8000/docs`

---

## 📂 Project Structure

```
upstage6/
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

```

## 🔌 API Overview

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/documents/upload` | 문서 업로드 및 텍스트 추출 |
| `GET` | `/api/documents` | 업로드된 문서 목록 조회 |
| `POST` | `/api/analysis/run/{id}` | 멀티 에이전트 분석 파이프라인 실행 |
| `GET` | `/api/analysis/{id}` | 최종 리포트 및 상세 데이터(하이라이트 정보) 조회 |

---

## 📜 License

This project is developed for the **Upstage AI Lab** program.

```

```
