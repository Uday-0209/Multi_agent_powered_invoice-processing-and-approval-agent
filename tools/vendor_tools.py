class VendorTools:

    def verify_vendor(self, vendor, db_tools):

        po = db_tools.db.query(
            db_tools.db.PurchaseOrder
        ).filter_by(vendor_name=vendor).first()

        return po is not None