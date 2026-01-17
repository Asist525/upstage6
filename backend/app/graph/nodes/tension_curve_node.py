# app/graph/nodes/tension_curve_node.py
from app.agents import TensionCurveAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

tension_curve_agent = TensionCurveAgent()

@traceable_timed(name="tension_curve")
def tension_curve_node(state: AgentState) -> AgentState:
    logger.info("긴장감 분석: [START]")
    result = tension_curve_agent.run(
        state.get("split_text"),
        persona=state.get("reader_persona")
    )
    logger.info("긴장감 분석: [END]")
    return {
        "tension_curve_result": result
    }
