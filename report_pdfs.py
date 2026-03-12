from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors
import os

os.makedirs("uploads", exist_ok=True)

styles = getSampleStyleSheet()

def create_invoice(file, vendor, invoice_no, items, vat):
    doc = SimpleDocTemplate(file, pagesize=A4)

    subtotal = sum(q*p for _,q,p in items)
    vat_amt = subtotal * vat
    total = subtotal + vat_amt

    data = [["Description","Qty","Price","Total"]]

    for desc,q,p in items:
        data.append([desc,q,f"€{p}",f"€{q*p}"])

    data += [
        ["","","Subtotal",f"€{subtotal}"],
        ["","",f"VAT {int(vat*100)}%",f"€{vat_amt}"],
        ["","","TOTAL",f"€{total}"]
    ]

    table = Table(data, colWidths=[8*cm,2*cm,3*cm,3*cm])
    table.setStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
    ])

    story = [
        Paragraph(f"<b>Vendor:</b> {vendor}", styles["Normal"]),
        Paragraph(f"<b>Invoice:</b> {invoice_no}", styles["Normal"]),
        Spacer(1,20),
        table
    ]

    doc.build(story)

create_invoice(
"uploads/invoice_normal.pdf",
"TechNova Solutions Ltd",
"INV-2025-001",
[("Cloud Hosting",3,1500),("Tech Support",1,500)],
0.10
)

create_invoice(
"uploads/invoice_large.pdf",
"Industrial Machinery Group",
"INV-8801",
[("Hydraulic Press",2,45000),("Installation",1,8000)],
0.14
)

create_invoice(
"uploads/invoice_suspicious.pdf",
"Global Trade Hub",
"992134",
[("Consulting Fee",1,25000)],
0.10
)

create_invoice(
"uploads/invoice_fake.pdf",
"QuickPay Solutions",
"FAKE-9922",
[("Service Charges",1,85000)],
0.10
)

create_invoice(
"uploads/invoice_mismatch.pdf",
"Metro Data Services",
"INV-3301",
[("Data Processing",2,2000)],
0.10
)

print("Invoices created in uploads/")