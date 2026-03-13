from tools.db_tools import DBTools
from utils.event_logger import log_event


class ValidationAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state: dict):

        # If not invoice, skip validation
        if state.get("document_type") != "invoice":
            return {}

        po_number = state.get("po_number")

        po = self.db_tools.get_purchase_order(po_number)

        if not po:

            result = {
                "validation_status": "invalid",
                "validation_reason": "Invoice received without purchase order"
            }

            log_event(
                state,
                "validation",
                result
            )

            return result

        if float(state.get("amount", 0)) != float(po.amount):

            result = {
                "validation_status": "invalid",
                "validation_reason": "Invoice amount mismatch"
            }

            log_event(
                state,
                "validation",
                result
            )

            return result

        result = {
            "validation_status": "valid"
        }

        log_event(
            state,
            "validation",
            result
        )

        return result