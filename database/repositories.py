from sqlalchemy.orm import Session
from database.models import PurchaseOrder, Invoice, Receipt


def create_purchase_order(db: Session, data: dict):

    po = PurchaseOrder(
        po_number=data.get("po_number"),
        company_name=data.get("company"),
        vendor_name=data.get("vendor"),
        item=data.get("item"),
        quantity=data.get("quantity"),
        amount=data.get("amount"),
        status="uploaded"
    )

    db.add(po)
    db.commit()
    db.refresh(po)

    return po


def create_receipt(db: Session, data: dict):

    receipt = Receipt(
        receipt_number=data.get("receipt_number"),
        invoice_number=data.get("invoice_number"),
        amount_paid=data.get("amount_paid"),
        payment_date=data.get("payment_date"),
        status="uploaded"
    )

    db.add(receipt)
    db.commit()
    db.refresh(receipt)

    return receipt


def get_purchase_order(db: Session, po_number: str):

    return db.query(PurchaseOrder)\
        .filter(PurchaseOrder.po_number == po_number)\
        .first()


def get_invoice(db: Session, invoice_number: str):

    return db.query(Invoice)\
        .filter(Invoice.invoice_number == invoice_number)\
        .first()