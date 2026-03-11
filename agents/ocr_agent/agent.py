from services.ocr_service import extract_text_from_pdf


class OCRAgent:

    def run(self, state: dict):
        
        file_path = state["file_path"]

        text = extract_text_from_pdf(file_path)

        return {
            **state,
            "ocr_text": text
        }