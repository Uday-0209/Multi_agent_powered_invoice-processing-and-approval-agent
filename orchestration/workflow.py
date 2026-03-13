# from langgraph.graph import StateGraph
# from orchestration.state import WorkFlowState
# from orchestration.router import route_document
# import dspy_programs.config

# from agents.ocr_agent.agent import OCRAgent
# from agents.extraction_agent.agent import ExtractionAgent
# from agents.fraud_agent.agent import FraudAgent
# from agents.decision_agent.agent import DecisionAgent
# from agents.human_review_agent.agent import HumanReviewAgent
# from agents.document_intake_agent.agent import DocumentIntakeAgent
# from agents.notification_agent.agent import NotificationAgent
# from agents.audit_agent.agent import AuditAgent
# from agents.validation_agent.agent import ValidationAgent
# from agents.classification_agent.agent import ClassificationAgent
# from agents.policy_agent.agent import PolicyAgent
# from agents.vendor_verification_agent.agent import VendorVerificationAgent
# from agents.company_verification_agnet.agent import CompanyVerificationAgent
# from agents.payment_verification_agent.agent import PaymentVerificationAgent


# def build_workflow():
    
#     graph = StateGraph(WorkFlowState)
    
#     ocr = OCRAgent()
#     extraction = ExtractionAgent()
#     fraud = FraudAgent()
#     decision = DecisionAgent()
#     human_review = HumanReviewAgent()
#     notification = NotificationAgent()
#     audit = AuditAgent()
#     validation = ValidationAgent()
#     classification = ClassificationAgent()
#     policy = PolicyAgent()
#     vendor_verification = VendorVerificationAgent()
#     document_intake = DocumentIntakeAgent()
#     company = CompanyVerificationAgent()
#     payment = PaymentVerificationAgent()
    
#     graph.add_node("intake", document_intake.run)
#     graph.add_node('ocr', ocr.run)
#     graph.add_node('extraction', extraction.run)
#     graph.add_node("classification", classification.run)
    
#     graph.add_node("vendor_verification", vendor_verification.run)
#     graph.add_node("company_verification", company.run)
#     graph.add_node("validation", validation.run)
#     graph.add_node('fraud', fraud.run)
#     graph.add_node("policy", policy.run)
#     graph.add_node("payment_verification", payment.run)
    
#     graph.add_node('decision', decision.run)   
#     graph.add_node("notification", notification.run)
     
#     graph.add_node("audit", audit.run)
#     graph.add_node('human_review', human_review.run)
    
    
      
    
#     graph.set_entry_point('intake')
    
#     graph.add_edge('intake', 'ocr')        
#     graph.add_edge('ocr', 'extraction')
#     graph.add_edge('extraction', 'classification')
#     graph.add_conditional_edges(
#         'classification',
#         route_document,
#         {
#             "po_pipeline": "vendor_verification",
#             "invoice_pipeline": "vendor_verification",
#             "receipt_pipeline": "vendor_verification"
#         }
#     )
#     graph.add_edge('vendor_verification', 'company_verification')
#     graph.add_edge('company_verification', 'validation')
#     graph.add_edge('validation', 'fraud')
#     graph.add_edge('fraud', 'policy')
#     graph.add_edge('policy', 'payment_verification')
#     graph.add_edge('payment_verification', 'decision')
#     graph.add_edge('decision', 'notification')
    
#     graph.set_finish_point("notification")
    
#     return graph.compile()


from langgraph.graph import StateGraph, END
from orchestration.state import WorkFlowState
from orchestration.router import document_router

import dspy_programs.config

# agents
from agents.document_intake_agent.agent import DocumentIntakeAgent
from agents.ocr_agent.agent import OCRAgent
from agents.extraction_agent.agent import ExtractionAgent
from agents.classification_agent.agent import ClassificationAgent

from agents.vendor_verification_agent.agent import VendorVerificationAgent
from agents.company_verification_agent.agent import CompanyVerificationAgent

from agents.validation_agent.agent import ValidationAgent
from agents.fraud_agent.agent import FraudAgent
from agents.policy_agent.agent import PolicyAgent
from agents.payment_verification_agent.agent import PaymentVerificationAgent

from agents.decision_agent.agent import DecisionAgent
from agents.notification_agent.agent import NotificationAgent

#agents to save the data to the database
from agents.SaveInvoiceAgent import SaveInvoiceAgent
from agents.savePurchaseOrderAgent import SavePurchaseOrderAgent
from agents.SaveReceiptAgent import SaveReceiptAgent

def build_workflow():

    graph = StateGraph(WorkFlowState)

    # instantiate agents
    intake = DocumentIntakeAgent()
    ocr = OCRAgent()
    extract = ExtractionAgent()
    classify = ClassificationAgent()

    vendor = VendorVerificationAgent()
    company = CompanyVerificationAgent()

    validation = ValidationAgent()
    fraud = FraudAgent()
    policy = PolicyAgent()
    payment = PaymentVerificationAgent()

    decision = DecisionAgent()
    notify = NotificationAgent()
    save_invoice = SaveInvoiceAgent()
    save_po = SavePurchaseOrderAgent()
    save_receipt = SaveReceiptAgent()


    # -------------------------
    # SHARED PIPELINE
    # -------------------------

    graph.add_node("intake", intake.run)
    graph.add_node("ocr", ocr.run)
    graph.add_node("extraction", extract.run)
    graph.add_node("classification", classify.run)

    # -------------------------
    # PO PIPELINE
    # -------------------------

    graph.add_node("po_vendor_verification", vendor.run)
    graph.add_node("po_company_verification", company.run)
    graph.add_node("po_fraud", fraud.run)
    graph.add_node("po_validation", validation.run)
    graph.add_node("po_policy", policy.run)
    graph.add_node("po_save", save_po.run)

    # -------------------------
    # INVOICE PIPELINE
    # -------------------------

    graph.add_node("invoice_vendor_verification", vendor.run)
    graph.add_node("invoice_company_verification", company.run)
    graph.add_node("invoice_validation", validation.run)
    graph.add_node("invoice_policy", policy.run)
    graph.add_node("invoice_save", save_invoice.run)

    # -------------------------
    # RECEIPT PIPELINE
    # -------------------------

    graph.add_node("receipt_vendor_verification", vendor.run)
    graph.add_node("receipt_company_verification", company.run)
    graph.add_node("receipt_validation", validation.run)
    graph.add_node("receipt_policy", policy.run)
    graph.add_node("receipt_payment", payment.run)
    graph.add_node("receipt_save", save_receipt.run)

    # -------------------------
    # FINAL
    # -------------------------

    graph.add_node("decision", decision.run)
    graph.add_node("notification", notify.run)

    # ENTRY
    graph.set_entry_point("intake")

    graph.add_edge("intake", "ocr")
    graph.add_edge("ocr", "extraction")
    graph.add_edge("extraction", "classification")

    # ROUTER
    graph.add_conditional_edges(
        "classification",
        document_router,
        {
            "po_flow": "po_vendor_verification",
            "invoice_flow": "invoice_vendor_verification",
            "receipt_flow": "receipt_vendor_verification",
        }
    )

    # -------------------------
    # PO FLOW
    # -------------------------

    graph.add_edge("po_vendor_verification", "po_company_verification")
    graph.add_edge("po_company_verification", "po_fraud")
    graph.add_edge("po_fraud", "po_validation")
    graph.add_edge("po_validation", "po_policy")
    graph.add_edge("po_policy", "po_save")
    graph.add_edge("po_save", "decision")

    # -------------------------
    # INVOICE FLOW
    # -------------------------

    graph.add_edge("invoice_vendor_verification", "invoice_company_verification")
    graph.add_edge("invoice_company_verification", "invoice_validation")
    graph.add_edge("invoice_validation", "invoice_policy")
    graph.add_edge("invoice_policy", "invoice_save")
    graph.add_edge("invoice_save", "decision")

    # -------------------------
    # RECEIPT FLOW
    # -------------------------

    graph.add_edge("receipt_vendor_verification", "receipt_company_verification")
    graph.add_edge("receipt_company_verification", "receipt_validation")
    graph.add_edge("receipt_validation", "receipt_policy")
    graph.add_edge("receipt_policy", "receipt_payment")
    graph.add_edge("receipt_payment", "receipt_save")
    graph.add_edge("receipt_save", "decision")

    # FINAL

    graph.add_edge("decision", "notification")
    graph.add_edge("notification", END)

    return graph.compile()

def debug_node(name):

    def wrapper(state):

        print(f"RUNNING NODE: {name}")

        return state

    return wrapper