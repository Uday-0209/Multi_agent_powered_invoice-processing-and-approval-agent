from tools.db_tools import DBTools
from database.models import PurchaseOrder


class VendorVerificationAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state: dict):

        print("Running Vendor Verification Agent")

        vendor = state.get("vendor")
        po_number = state.get("po_number")

        if not po_number:
            state["vendor_verified"] = False
            return state

        po = self.db_tools.db.query(PurchaseOrder).filter_by(
            po_number=po_number
        ).first()

        verified = po is not None

        return {
            **state,
            "vendor_verified": verified
        }