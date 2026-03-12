from langgraph.graph import StateGraph
from orchestration.state import WorkFlowState
from orchestration.router import route_document
import dspy_programs.config

from agents.ocr_agent.agent import OCRAgent
from agents.extraction_agent.agent import ExtractionAgent
from agents.fraud_agent.agent import FraudAgent
from agents.decision_agent.agent import DecisionAgent
from agents.human_review_agent.agent import HumanReviewAgent
from agents.document_intake_agent.agent import DocumentIntakeAgent
from agents.notification_agent.agent import NotificationAgent
from agents.audit_agent.agent import AuditAgent
from agents.validation_agent.agent import ValidationAgent
from agents.classification_agent.agent import ClassificationAgent
from agents.policy_agent.agent import PolicyAgent
from agents.vendor_verification_agent.agent import VendorVerificationAgent
from agents.company_verification_agnet.agent import CompanyVerificationAgent
from agents.payment_verification_agent.agent import PaymentVerificationAgent


def build_workflow():
    
    graph = StateGraph(WorkFlowState)
    
    ocr = OCRAgent()
    extraction = ExtractionAgent()
    fraud = FraudAgent()
    decision = DecisionAgent()
    human_review = HumanReviewAgent()
    notification = NotificationAgent()
    audit = AuditAgent()
    validation = ValidationAgent()
    classification = ClassificationAgent()
    policy = PolicyAgent()
    vendor_verification = VendorVerificationAgent()
    document_intake = DocumentIntakeAgent()
    company = CompanyVerificationAgent()
    payment = PaymentVerificationAgent()
    
    graph.add_node("intake", document_intake.run)
    graph.add_node('ocr', ocr.run)
    graph.add_node('extraction', extraction.run)
    graph.add_node("classification", classification.run)
    
    graph.add_node("vendor_verification", vendor_verification.run)
    graph.add_node("company_verification", company.run)
    graph.add_node("validation", validation.run)
    graph.add_node('fraud', fraud.run)
    graph.add_node("policy", policy.run)
    graph.add_node("payment_verification", payment.run)
    
    graph.add_node('decision', decision.run)   
    graph.add_node("notification", notification.run)
     
    graph.add_node("audit", audit.run)
    graph.add_node('human_review', human_review.run)
    
    
      
    
    graph.set_entry_point('intake')
    
    graph.add_edge('intake', 'ocr')        
    graph.add_edge('ocr', 'extraction')
    graph.add_edge('extraction', 'classification')
    graph.add_conditional_edges(
        'classification',
        route_document,
        {
            "po_pipeline": "vendor_verification",
            "invoice_pipeline": "vendor_verification",
            "receipt_pipeline": "vendor_verification"
        }
    )
    graph.add_edge('vendor_verification', 'company_verification')
    graph.add_edge('company_verification', 'validation')
    graph.add_edge('validation', 'fraud')
    graph.add_edge('fraud', 'policy')
    graph.add_edge('policy', 'payment_verification')
    graph.add_edge('payment_verification', 'decision')
    graph.add_edge('decision', 'notification')
    
    graph.set_finish_point("notification")
    
    return graph.compile()