import dspy 

class DecisionReasoning(dspy.Signature):
    
    vendor = dspy.InputField()
    total = dspy.InputField()
    invoice_number = dspy.InputField()
    
    fraud_score = dspy.InputField()
    fraud_reason = dspy.InputField()
    
    decision = dspy.OutputField(desc = "approve | manual_review | reject")
    explanation = dspy.OutputField(desc = "reason for the decision")