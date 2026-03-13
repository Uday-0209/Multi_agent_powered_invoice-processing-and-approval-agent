
from dspy_programs.prompt_optimizer import optmize_extractor
from utils.event_logger import log_event 

class ExtractionAgent:
    def __init__(self) -> None:
        self.program = optmize_extractor()
        
    def run(self, state: dict):
                
        result  = self.program(text = state["ocr_text"])    
        
        output = {
            "vendor": result.vendor,
            "total": result.total

        }   
        
        
        log_event(
            state,
            "data_extraction",
            output
        )
        return output