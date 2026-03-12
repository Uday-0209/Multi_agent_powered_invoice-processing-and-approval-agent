from database.connection import SessionLocal
from database.models import PurchaseOrder, Invoice, Receipt


class DBTools:

    def __init__(self):
        self.db = SessionLocal()


    def get_purchase_order(self, po_number):

        return self.db.query(PurchaseOrder).filter_by(
            po_number=po_number
        ).first()


    def get_invoice(self, invoice_number):

        return self.db.query(Invoice).filter_by(
            invoice_number=invoice_number
        ).first()


    def save_purchase_order(self, data):

        po = PurchaseOrder(
            po_number=data["po_number"],
            company_name=data["company"],
            vendor_name=data["vendor"],
            item=data["item"],
            quantity=data["quantity"],
            amount=data["amount"],
            status="approved"
        )

        self.db.add(po)
        self.db.commit()


    def save_invoice(self, data):

        invoice = Invoice(
            invoice_number=data["invoice_number"],
            po_number=data["po_number"],
            company_name=data["company"],
            vendor_name=data["vendor"],
            amount=data["amount"],
            status="approved"
        )

        self.db.add(invoice)
        self.db.commit()


    def save_receipt(self, data):

        receipt = Receipt(
            receipt_number=data["receipt_number"],
            invoice_number=data["invoice_number"],
            amount_paid=data["amount_paid"],
            payment_date=data["payment_date"],
            status="verified"
        )

        self.db.add(receipt)
        self.db.commit()