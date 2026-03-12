
from dspy_programs.prompt_optimizer import optmize_extractor

class ExtractionAgent:
    def __init__(self) -> None:
        self.program = optmize_extractor()
        
    def run(self, state: dict):
                
        result  = self.program(text = state["ocr_text"])
        
        return {
            **state,
            "vendor": result.vendor,
            "total": result.total
        } 