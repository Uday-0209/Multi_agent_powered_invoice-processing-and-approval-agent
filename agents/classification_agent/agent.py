import dspy 
from dspy_programs.doc_classifier import DocumentClassification
from utils.event_logger import log_event

class ClassificationAgent:
    
    def run(self, state):
        
        classifier = dspy.Predict(DocumentClassification)
        
        result = classifier(text = state['ocr_text'])
        
        output = {
            
            "document_type": result.doc_type
        }
        log_event(
            state,
            "document_classification",
            output
        )
        return output