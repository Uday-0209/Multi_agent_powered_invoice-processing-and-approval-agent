import dspy
from dspy_programs.fraud_detection import FraudDetection

class FraudAgent:
    
    def run(self, state:dict):
        
        fraud_model = dspy.Predict(FraudDetection)
        result = fraud_model(
            vendor = state["vendor"],
            total = state["total"]
        )
        return {
            **state,
            "fraud_score": result.risk_score
        }