from typing import TypedDict, List, Dict, Annotated
from langgraph.graph import StateGraph
from langgraph.channels import LastValue

class WorkFlowState(TypedDict):
    
    workflow_id: Annotated[str, LastValue(str)]
    file_path: str
    ocr_text: str
    
    vendor: str
    total: str
    
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
    vendor_verified: bool
    po_number: str
    company_verified: bool    
    
    events: List[Dict]
    
    