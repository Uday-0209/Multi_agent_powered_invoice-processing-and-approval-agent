from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True)
    po_number = Column(String)
    company_name = Column(String)
    vendor_name = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    amount = Column(String)
    status = Column(String)
    
class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String)
    vendor_name = Column(String)
    company_name = Column(String)
    amount = Column(String)
    po_number = Column(String)
    status = Column(String)
    
class Receipt(Base):

    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True)
    receipt_number = Column(String)
    invoice_number = Column(String)
    amount_paid = Column(String)
    payment_date = Column(String)

    status = Column(String)