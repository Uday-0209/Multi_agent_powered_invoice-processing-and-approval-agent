from tools.db_tools import DBTools

class PaymentVerificationAgent:

    def __init__(self, db_tools: DBTools):
        self.db_tools = db_tools

    def run(self, state):

        if state["document_type"] != "receipt":
            return state

        invoice_number = state.get("invoice_number")

        invoice = self.db_tools.get_invoice(invoice_number)

        if not invoice:

            state["payment_status"] = "invalid"
            state["payment_reason"] = "Receipt received without invoice"

            return state

        if float(state["amount_paid"]) != float(invoice.amount):

            state["payment_status"] = "invalid"
            state["payment_reason"] = "Receipt payment mismatch"

            return state

        state["payment_status"] = "valid"

        return state