import dspy 
from dspy.teleprompt import BootstrapFewShot
from dspy_programs.invoice_extractor import InvoiceExtraction
from dspy_programs.example import trainset

def optmize_extractor():
    
    extractor = dspy.Predict(InvoiceExtraction)
    
    optimizer = BootstrapFewShot()
    
    compiled_prompt = optimizer.compile(
        extractor,
        trainset = trainset
    )
    
    return compiled_prompt