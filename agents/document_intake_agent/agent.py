class DocumentIntakeAgent:
    def run(self, state: dict):
        file_path = state["file_path"]
        
        if not file_path.endswith(".pdf"):
            raise ValueError("only pdf files are supported")
        return {
            **state,
            "document_status": "intake_completed"
        }