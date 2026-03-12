import dspy 

class DocumentClassification(dspy.Signature):
    
    text = dspy.InputField()
    
    doc_type = dspy.OutputField(desc = "invoice | receipt | purchase_order")