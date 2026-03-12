import dspy 
from dspy_programs.doc_classifier import DocumentClassification

class ClassificationAgent:
    
    def run(self, state):
        
        classifier = dspy.Predict(DocumentClassification)
        
        result = classifier(text = state['ocr_text'])
        
        return {
            **state,
            "doc_type": result.doc_type
        }