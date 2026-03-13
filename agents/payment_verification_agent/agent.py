from tools.db_tools import DBTools
from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "PaymentVerificationAgent")
class PaymentVerificationAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state):

        # If not receipt, do nothing
        if state.get("document_type") != "receipt":
            return {}

        invoice_number = state.get("invoice_number")

        invoice = self.db_tools.get_invoice(invoice_number)

        if not invoice:

            result = {
                "payment_status": "invalid",
                "payment_reason": "Receipt received without invoice"
            }

            log_event(
                state,
                "payment_verification",
                result
            )

            return result

        if float(state.get("amount_paid", 0)) != float(invoice.amount):

            result = {
                "payment_status": "invalid",
                "payment_reason": "Receipt payment mismatch"
            }

            log_event(
                state,
                "payment_verification",
                result
            )

            return result

        result = {
            "payment_status": "valid"
        }

        log_event(
            state,
            "payment_verification",
            result
        )

        return result