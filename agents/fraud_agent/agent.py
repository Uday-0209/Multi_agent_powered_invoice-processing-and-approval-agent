from dspy_programs.fraud_optimizer import optimize_fraud_detector

class FraudAgent:
    def __init__(self) -> None:
        self.program = optimize_fraud_detector()
    
    def run(self, state:dict):
        
        result = self.program(
            vendor = state["vendor"],
            total = state["total"],
            invoice_number=state.get("invoice_number", "")
        )
        try:
            fraud_score = int(result.risk_score)
        except:
            fraud_score = 0   # fallback if LLM returns invalid value
            
        return {
            **state,
            "fraud_score": fraud_score,
            "fraud_reason": result.reason
        }