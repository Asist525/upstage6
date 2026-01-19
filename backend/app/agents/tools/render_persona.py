from app.agents.base import BaseAgent
from app.llm.chat import chat

class ReaderPersonaAgent(BaseAgent):
    """
    독자 페르소나 생성 에이전트
    - 평가/수정/판단 x
    - 독자 관점 맥락 생성 o
    """

    name = "reader-persona"

    def run(self, context: dict) -> dict:
        user_persona = context.get("user_persona")
        text_preview = context.get("text_preview", "")
        meta = context.get("meta", {})

        system = """
너는 글의 타겟 독자를 시뮬레이션하기 위한 '가상 독자(페르소나) 생성기'다.
주어진 정보를 바탕으로, 이 글을 읽고 피드백을 줄 가장 적절한 가상 인물을 구체적으로 설계하라.
반드시 유효한 JSON 포맷으로만 출력해야 한다.
"""

        # 사용자 지정 페르소나가 있는 경우
        if user_persona and (user_persona.get("name") or user_persona.get("desc")):
            base_prompt = f"""
사용자가 지정한 다음 가상 독자 설정을 바탕으로 페르소나를 구체화하라.
사용자의 의도를 최대한 반영하되, 원고 내용에 맞게 구체적인 성격과 관점을 보완하라.

[사용자 지정 설정]
- 이름/역할: {user_persona.get("name", "미지정")}
- 상세 설정: {user_persona.get("desc", "미지정")}
"""
        else:
            # 자동 생성 모드
            base_prompt = f"""
다음 원고(앞부분 3000자)를 분석하여, 이 글의 잠재적 타겟 독자 중 
'가장 건설적이고 날카로운 피드백을 줄 수 있는' 대표 페르소나 1명을 생성하라.
장르와 문체에 어울리는 직업과 성격을 부여하라.
"""

        prompt = f"""
{base_prompt}

[원고 정보]
- 메타데이터: {meta}
- 본문 프리뷰(일부분):
{text_preview[:2000]}...

[출력 JSON 형식]
{{
  "persona": {{
    "name": "이름 (가명 또는 별명)",
    "role": "직업 또는 역할 (예: 깐깐한 편집자, 로맨스 소설 매니아 등)",
    "age_group": "연령대 (예: 20대 후반)",
    "personality": "성격 묘사 (한 문장)",
    "reading_taste": "평소 독서 취향",
    "background_knowledge": "관련 배경지식 수준",
    "feedback_style": "피드백 스타일 (예: 직설적, 감성적, 논리적)",
    "goals": ["이 글에서 기대하는 점 1", "기대하는 점 2"],
    "concerns": ["우려하는 점 또는 싫어하는 요소"]
  }}
}}
"""
        response = chat(prompt, system=system)
        return self._safe_json_load(response)