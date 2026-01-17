# app/graph/nodes/spelling_node.py
from app.agents import SpellingAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

spelling_agent = SpellingAgent()

@traceable_timed(name="spelling")
def spelling_node(state: AgentState) -> AgentState:
    logger.info("맞춤법 검사: [START]")
    result = spelling_agent.run(state.get("split_text"))
    logger.info("맞춤법 검사: [END]")
    return {
        "spelling_result": result
    }
