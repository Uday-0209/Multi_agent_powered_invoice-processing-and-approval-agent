from dspy_programs.decision_optimizer import optimize_decision_model
from tools.db_tools import DBTools
from tools.notification_tools import NotificationTools

class DecisionAgent:

    def __init__(self):
        self.program = optimize_decision_model()
        self.db_tools = DBTools()
        self.notification_tools = NotificationTools()

    def run(self, state: dict):

        result = self.program(
            vendor=state["vendor"],
            total=state["total"],
            fraud_score=str(state["fraud_score"]),
            fraud_reason=state["fraud_reason"]
        )
        
        decision = result.decision
        state = {**state,
            "decision": result.decision,
            "explanation": result.explanation
        }
        
        if decision == "approve":
            doc_type = state.get['doc_type']
            
            if doc_type == "purchase_order":
                self.db_tools.save_purchase_order(state)
            elif doc_type == "invoice":
                self.db_tools.save_invoice(state)
            elif doc_type == "receipt":
                self.db_tools.save_receipt(state)
                
        self.notification_tools.send_notification({
            "document_type": state["document_type"],
            "vendor": state["vendor"],
            "total": state["total"],
            "decision": decision
        })
        
        return state