# app/graph/nodes/causality_node.py
from app.agents import CausalityEvaluatorAgent
from app.graph.state import AgentState
from app.observability.langsmith import traceable_timed
import logging

logger = logging.getLogger(__name__)

causality_agent = CausalityEvaluatorAgent()

@traceable_timed(name="logic")
def causality_node(state: AgentState) -> AgentState:
    logger.info("개연성 분석: [START]")
    
    result = causality_agent.run(
        state.get("split_text"),
        global_summary=state.get("global_summary"),
        persona=state.get("reader_persona")
    )
    logger.info("개연성 분석: [END]")
    return {
        "logic_result": result
    }

