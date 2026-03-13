from tools.db_tools import DBTools
from database.models import PurchaseOrder
from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "VendorVerificationAgent")
class VendorVerificationAgent:

    def __init__(self):
        self.db_tools = DBTools()

    def run(self, state: dict):

        print("Running Vendor Verification Agent")

        vendor = state.get("vendor")
        po_number = state.get("po_number")

        if not po_number:
            output = {"vendor_verified": False}
            return output

        po = self.db_tools.db.query(PurchaseOrder).filter_by(
            po_number=po_number
        ).first()

        verified = po is not None

        
           
        output = {"vendor_verified":  verified}
        
        log_event(
            state,
            "vendor_verification",
            {"verified": verified})
        return output