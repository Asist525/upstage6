# app/graph/nodes/tone_node.py
from app.agents import ToneEvaluatorAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

tone_agent = ToneEvaluatorAgent()

@traceable_timed(name="tone")
def tone_node(state: AgentState) -> AgentState:
    logger.info("톤앤매너 분석: [START]")
    result = tone_agent.run(
        state.get("split_text"),
        global_summary=state.get("global_summary"),
        persona=state.get("reader_persona")
    )
    logger.info("톤앤매너 분석: [END]")
    return {
        "tone_result": result
    }
