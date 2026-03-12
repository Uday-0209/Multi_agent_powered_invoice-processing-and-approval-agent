from sqlalchemy import Column, Integer, String, Float
from database.session import Base


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True)
    po_number = Column(String)
    company_name = Column(String)
    vendor_name = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    amount = Column(Float)
    status = Column(String)


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String)
    vendor_name = Column(String)
    company_name = Column(String)
    amount = Column(Float)
    po_number = Column(String)
    status = Column(String)


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True)
    receipt_number = Column(String)
    invoice_number = Column(String)
    amount_paid = Column(Float)
    payment_date = Column(String)
    status = Column(String)