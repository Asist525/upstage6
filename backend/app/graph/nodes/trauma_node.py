# app/graph/nodes/trauma_node.py
from app.agents import TraumaAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

trauma_agent = TraumaAgent()

@traceable_timed(name="trauma")
def trauma_node(state: AgentState) -> AgentState:
    logger.info("트라우마 분석: [START]")
    result = trauma_agent.run(
        state.get("split_text")
    )
    logger.info("트라우마 분석: [END]")
    return {
        "trauma_result": result
    }
