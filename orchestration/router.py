def route_decision(state):

    decision = state["decision"]

    if decision == "manual_review":
        return "human_review"

    return "end"

def route_document(state):

    doc_type = state["document_type"]

    if doc_type == "purchase_order":
        return "po_pipeline"

    if doc_type == "invoice":
        return "invoice_pipeline"

    if doc_type == "receipt":
        return "receipt_pipeline"

    return "end"