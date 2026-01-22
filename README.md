# 🖋️ TEAM CONTEXTOR

> **원고 분석을 위한 지능형 멀티 에이전트 시스템 (Intelligent Multi-Agent System for Manuscript Analysis)**
> 사용자가 업로드한 원고(PDF/DOCX/TXT/MD)를 분석하여 가독성, 톤, 인과관계, 부적절한 표현 등을 진단하고, 종합적인 전문가 리포트를 제공합니다.

---

## 👤 Maintainer Info (Portfolio Fork)

- **Maintainer**: 박건원 (GitHub: [Asist525](https://github.com/Asist525))
- **Role**: Backend Engineering (Primary) / Frontend Optimization
- **Context**: 본 레포지토리는 **TEAM CONTEXTOR (TEAM SIX)** 해커톤 프로젝트를 기반으로, **개인 포트폴리오 및 기술 데모 목적**으로 포크(Fork)하여 관리하는 버전입니다.

---

## 🏆 My Verified Contributions

> **핵심 기여 사항**
> 단순 참여가 아닌, **직접 설계하고 코드로 구현한 핵심 기능**입니다.
> Evidence: [Commits by Asist525](https://github.com/Asist525/upstage6/commits/main?author=Asist525)

### 🧠 1. Backend Engineering & MLOps (Primary)
**FastAPI**와 **LangGraph**를 기반으로 멀티 에이전트 파이프라인의 안정성과 평가 시스템을 주도적으로 구축했습니다.

- **Eval / QA Scoring 파이프라인 확장**
  - 단순 LLM 호출을 넘어, 결과의 신뢰도를 측정하는 **Self-Evaluation System**을 설계했습니다.
  - **LangGraph Node 구성**: `Spelling Evaluator` 도입 및 `eval_report`, `pipeline_runner` 구조를 정립하여 분석-평가 순환 루프를 완성했습니다.
- **Observability (LangSmith) 도입**
  - 프로덕션 레벨의 디버깅을 위해 **LangSmith**를 연동했습니다.
  - `analysis_runner` 및 `eval_runner`의 실행 경로를 계측(Tracing)하여 토큰 사용량 및 레이턴시를 모니터링할 수 있는 환경을 구축했습니다.
- **Split/Chunking 기반 분석 안정화**
  - 대용량 텍스트 처리 시 발생하는 컨텍스트 누락을 방지하기 위해 `SplitAgent` 로직을 개선했습니다.
  - 문장 단위 Chunking 및 입력 포맷 정규화를 통해 후속 에이전트(Tone, Narrative 등)의 분석 정확도를 높였습니다.

### 🎨 2. Frontend Optimization (Secondary)
백엔드 로직을 사용자에게 직관적으로 전달하기 위한 UI/UX 개선 작업을 수행했습니다.

- **Highlight & Tooltip System**: 분석된 메타데이터를 원문 텍스트에 매핑하는 로직을 최적화하고, 가독성을 고려한 색상 팔레트를 적용했습니다.
- **UI Stabilization**: 리포트/스코어 패널의 토글 UX를 개선하고, 레이아웃 스크롤 및 JSX 렌더링 오류를 수정하여 데모 시연 품질을 확보했습니다.

---

### 🗝️ Key Commits (Evidence)
면접관님께서 **가장 중점적으로 보셔야 할 코드**입니다. (링크 클릭 시 Diff 확인 가능)

| Category | Commit | Description |
| :--- | :--- | :--- |
| **Architecture** | [`0e205be`](https://github.com/Asist525/upstage6/commit/0e205be6e22deca51cb3bc1afe87c79effeb9be4) | **Spelling Agent + Evaluator 체계 전환**: 평가 시스템 구조화 및 리포트 파이프라인 정립 |
| **Feature** | [`e81e52a`](https://github.com/Asist525/upstage6/commit/e81e52a9e9ab96e2055910acfbd1e44827cfb188) | **Eval Logic 확장**: Spelling Evaluator 도입 및 LangGraph 노드 연결 |
| **Ops** | [`bc1089b`](https://github.com/Asist525/upstage6/commit/bc1089b42d50887bf4e69f751596158f7239149c) | **Observability**: LangSmith 추적(Tracing) 설정 및 런타임 계측 코드 적용 |
| **Data** | [`44c5882`](https://github.com/Asist525/upstage6/commit/44c5882b8088a4253999cdd37a0dfafc8635c19e) | **Pipeline Stabilization**: Split Agent 청킹 로직 개선 및 대용량 처리 안정화 |
| **UI/UX** | [`3cb9120`](https://github.com/Asist525/upstage6/commit/3cb9120a748017626b95c0f900229e8fcf4ad29c) | **Visualization**: 하이라이트 렌더링 최적화 및 툴팁/반응형 UI 구현 |

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
| **Orchestration** | LangChain / LangGraph |
| **Database** | SQLite (SQLAlchemy) |
| **Parsing** | Upstage Document Parse, python-docx, pypdf |
| **Observability**| LangSmith |

### Frontend
| Category | Technology |
| :--- | :--- |
| **Framework** | React 18 (Vite) |
| **Rendering** | react-markdown, Custom Highlight logic |
| **Styling** | Tailwind CSS / Styled Components |

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
# .env 파일을 열어 UPSTAGE_API_KEY, LANGSMITH_API_KEY 등을 입력하세요.

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
