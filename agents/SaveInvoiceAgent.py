from tools.db_tools import DBTools
from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "SaveInvoiceAgent")
class SaveInvoiceAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state):

        if state.get("document_type") != "invoice":
            return {}

        self.db_tools.save_invoice({
            "invoice_number": state.get("invoice_number"),
            "po_number": state.get("po_number"),
            "company": state.get("company"),
            "vendor": state.get("vendor"),
            "amount": state.get("amount")
        })

        log_event(state, "invoice_saved", {
            "invoice_number": state.get("invoice_number")
        })

        print("INVOICE SAVED TO DATABASE")

        return {"invoice_saved": True}