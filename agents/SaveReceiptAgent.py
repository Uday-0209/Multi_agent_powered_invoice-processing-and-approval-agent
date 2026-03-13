from tools.db_tools import DBTools
from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "SaveReceiptAgent")
class SaveReceiptAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state):

        if state.get("document_type") != "receipt":
            return {}

        self.db_tools.save_receipt({
            "receipt_number": state.get("receipt_number"),
            "invoice_number": state.get("invoice_number"),
            "amount_paid": state.get("amount_paid"),
            "payment_date": state.get("payment_date")
        })

        log_event(state, "receipt_saved", {
            "receipt_number": state.get("receipt_number")
        })

        print("RECEIPT SAVED TO DATABASE")

        return {"receipt_saved": True}