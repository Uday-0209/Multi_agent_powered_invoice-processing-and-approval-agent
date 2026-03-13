from utils.event_logger import log_event
from services.ocr_service import extract_text_from_pdf


class OCRAgent:

    def run(self, state):

        print("Running OCR Agent")

        # 🔹 TEST MODE: if OCR text already exists skip OCR
        if state.get("ocr_text"):

            log_event(
                state,
                "ocr",
                {"ocr_text": state["ocr_text"]}
            )

            return {}

        # 🔹 PRODUCTION MODE: run OCR
        file_path = state.get("file_path")

        if not file_path:
            raise ValueError("OCR requires file_path or ocr_text")

        text = extract_text_from_pdf(file_path)

        log_event(
            state,
            "ocr",
            {"ocr_text": text}
        )

        return {"ocr_text": text}