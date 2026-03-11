import dspy 
from dspy_programs.invoice_extractor import InvoiceExtraction

class ExtractionAgent:
    def run(self, state: dict):
        
        text = state['ocr_text']
        
        extractor = dspy.Predict(InvoiceExtraction)
        
        
        result  = extractor(text = text)
        
        return {
            **state,
            "vendor": result.vendor,
            "total": result.totel
        } 