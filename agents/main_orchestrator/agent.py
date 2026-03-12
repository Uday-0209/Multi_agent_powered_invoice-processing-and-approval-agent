class MainOrchestratorAgent:

    def run(self, state):

        doc_type = state["document_type"]

        if doc_type == "purchase_order":
            return "po_pipeline"

        if doc_type == "invoice":
            return "invoice_pipeline"

        if doc_type == "receipt":
            return "receipt_pipeline"