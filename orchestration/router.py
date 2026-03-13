def document_router(state):

    doc_type = state.get("document_type")

    if doc_type == "purchase_order":
        return "po_flow"

    if doc_type == "invoice":
        return "invoice_flow"

    if doc_type == "receipt":
        return "receipt_flow"

    return "invoice_flow"