import dspy

class InvoiceExtraction(dspy.Signature):
    
    text = dspy.InputField()
    
    vendor = dspy.OutputField()
    
    total = dspy.OutputField()
    
    invoice_number = dspy.OutputField()