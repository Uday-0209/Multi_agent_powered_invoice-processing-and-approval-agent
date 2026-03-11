from sqlalchemy.orm import Session
from database.models import Invoice

def create_invoice(db: Session,  data: dict):
    invoice = Invoice(
        vendor=data.get("vendor"),
        total=data.get("total"),
        status="uploaded",
        raw_data=data
    )
    
    db.add(invoice)
    db.commit()
    
    return invoice