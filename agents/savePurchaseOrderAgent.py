from tools.db_tools import DBTools
from utils.event_logger import log_event


class SavePurchaseOrderAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state):

        if state.get("document_type") != "purchase_order":
            return {}

        self.db_tools.save_purchase_order({
            "po_number": state.get("po_number"),
            "company": state.get("company"),
            "vendor": state.get("vendor"),
            "item": state.get("item"),
            "quantity": state.get("quantity"),
            "amount": state.get("amount")
        })

        log_event(state, "po_saved", {"po_number": state.get("po_number")})

        print("PO SAVED TO DATABASE")

        return {"po_saved": True}