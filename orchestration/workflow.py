from langgraph.graph import StateGraph
from orchestration.state import WorkFlowState

from agents.ocr_agent.agent import OCRAgent
from agents.extraction_agent.agent import ExtractionAgent
from agents.fraud_agent.agent import FraudAgent
from agents.decision_agent.agent import DecisionAgent

def build_workflow():
    
    graph = StateGraph(WorkFlowState)
    
    ocr = OCRAgent()
    extraction = ExtractionAgent()
    fraud = FraudAgent()
    decision = DecisionAgent()
    
    graph.add_node('ocr', ocr.run)
    graph.add_node('extraction', extraction.run)
    graph.add_node('fraud', fraud.run)
    graph.add_node('decision', decision.run)
    
    graph.set_entry_point('ocr')
    
    graph.add_edge('ocr', 'extraction')
    graph.add_edge('extraction', 'fraud')
    graph.add_edge('fraud', 'decision')
    
    return graph.compile()