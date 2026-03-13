from dspy_programs.decision_optimizer import optimize_decision_model
from tools.db_tools import DBTools
from tools.notification_tools import NotificationTools
from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable
load_dotenv()

@traceable(name = "DecisionAgent")
class DecisionAgent:

    def __init__(self):
        self.program = optimize_decision_model()
        self.db_tools = DBTools()
        self.notification_tools = NotificationTools()

    def run(self, state: dict):

        result = self.program(
            vendor=state.get("vendor"),
            total=state.get("total"),
            fraud_score=str(state.get("fraud_score")),
            fraud_reason=state.get("fraud_reason")
        )
        
        decision = result.decision
        output = {
            "decision": result.decision,
            "explanation": result.explanation
        }
        
        if decision == "approve":
            doc_type = state.get('doc_type')
            
            if doc_type == "purchase_order":
                self.db_tools.save_purchase_order(state)
            elif doc_type == "invoice":
                self.db_tools.save_invoice(state)
            elif doc_type == "receipt":
                self.db_tools.save_receipt(state)
                
        self.notification_tools.send_notification({
            "document_type": state.get("document_type"),
            "vendor": state.get("vendor"),
            "total": state.get("total"),
            "decision": decision
        })
        log_event(
            state,
            "decision",
            output
        )
        
        return output