from tools import db_tools

class VendorVerificationAgent:
    def __init__(self, db_tools):
        self.db_tools = db_tools
    
    def run(self, state: dict):
        
        vendor = state['vendor']
        
        po = self.db_tools.db.query(
            state.get("po_number")
        ).first()
        
        verified = po is not None 
        
        return {
            **state,
            "vendor_verified": verified
        }