import uuid


def create_initial_state(file_path: str):

    return {
        "workflow_id": str(uuid.uuid4()),
        "file_path": file_path,
        "events": [],
        "document_type": None,
        "ocr_text": None,
        "vendor": None,
        "company": None,
        "po_number": None,
        "invoice_number": None,
        "amount": None,
        "amount_paid": None,
        "vendor_verified": None,
        "company_verified": None,
        "validation_status": None,
        "fraud_score": None,
        "fraud_reason": None,
        "payment_status": None,
        "decision": None,
        "decision_reason": None,
    }