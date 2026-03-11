import dspy

class FraudDetection(dspy.Signature):
    
    vendor = dspy.InputField()
    total = dspy.InputField()
    
    risk_score = dspy.OutputField()