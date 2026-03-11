from typing import TypedDict

class WorkFlowState(TypedDict):
    
    file_path: str
    ocr_text: str
    vendor: str
    total: str
    invoice_number: str
    fraud_score:str
    decision: str
    