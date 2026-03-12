import dspy

class FraudDetection(dspy.Signature):
    
    vendor = dspy.InputField()
    total = dspy.InputField()
    invoice_number = dspy.InputField()
    
    risk_score = dspy.OutputField(desc = "Fraud risk score from 0 to 100")
    
    reason = dspy.OutputField(desc = "Explaination of the risk score")