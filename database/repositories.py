from sqlalchemy.orm import Session
from database.models import Invoice


def create_invoice(db: Session, data: dict):

    invoice = Invoice(
        invoice_number=data.get("invoice_number"),
        vendor_name=data.get("vendor"),
        company_name=data.get("company"),
        amount=data.get("amount"),
        po_number=data.get("po_number"),
        status="uploaded"
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice