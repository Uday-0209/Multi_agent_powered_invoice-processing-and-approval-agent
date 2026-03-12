from services.ocr_service import extract_text_from_pdf


class OCRAgent:

    def run(self, state: dict):
        
        file_path = state["file_path"]

        text = extract_text_from_pdf(file_path)

        return {
            **state,
            "ocr_text": text
        }
# class OCRAgent:

#     def run(self, state):

#         print("Running OCR Agent")

#         # MOCK OCR OUTPUT
#         state["ocr_text"] = """
#         Purchase Order
#         Vendor: ABC Ltd
#         Company: XYZ Corp
#         Item: Steel Rod
#         Quantity: 200
#         Amount: 5000
#         """

#         return state