# app/graph/nodes/genre_cliche_node.py
from app.agents import GenreClicheAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

genre_cliche_agent = GenreClicheAgent()

@traceable_timed(name="genre_cliche")
def genre_cliche_node(state: AgentState) -> AgentState:
    logger.info("클리셰 분석: [START]")
    result = genre_cliche_agent.run(
        state.get("split_text"),
        global_summary=state.get("global_summary"),
        persona=state.get("reader_persona")
    )
    logger.info("클리셰 분석: [END]")
    return {
        "genre_cliche_result": result
    }
