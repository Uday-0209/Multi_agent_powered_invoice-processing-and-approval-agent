from tools.db_tools import DBTools

class ValidationAgent:

    def __init__(self, db_tools: DBTools):
        self.db_tools = db_tools

    def run(self, state):

        if state["document_type"] != "invoice":
            return state

        po_number = state.get("po_number")

        po = self.db_tools.get_purchase_order(po_number)

        if not po:

            state["validation_status"] = "invalid"
            state["validation_reason"] = "Invoice received without purchase order"

            return state

        if float(state["amount"]) != float(po.amount):

            state["validation_status"] = "invalid"
            state["validation_reason"] = "Invoice amount mismatch"

            return state

        state["validation_status"] = "valid"

        return state