from typing import TypedDict

class WorkFlowState(TypedDict):
    
    file_path: str
    ocr_text: str
    
    vendor: str
    total: str
    invoice_number: str
    
    fraud_score:str
    fraud_reason: str
    
    decision: str
    decision_reason: str
    
    status: str
    
    document_type: str

    po_number: str
    invoice_number: str

    amount: float
    amount_paid: float

    validation_status: str
    payment_status: str
    company: str
    