# from orchestration.workflow import build_workflow

# workflow = build_workflow()


# def test_purchase_order():

#     state = {
#         "file_path": "tests/sample_po.pdf",

#         "document_type": "purchase_order",

#         "po_number": "PO1001",

#         "vendor": "ABC Ltd",
#         "company": "XYZ Corp",

#         "item": "Steel Rod",
#         "quantity": 200,

#         "amount": 5000,

#         "invoice_number": None,
#         "receipt_number": None,

#         "amount_paid": None
#     }

#     result = workflow.invoke(state)

#     print("\nFINAL RESULT\n")
#     print(result)


# if __name__ == "__main__":
#     test_purchase_order()

from orchestration.workflow import build_workflow


workflow = build_workflow()


# def test_po():

#     state = {
#         "file_path": "tests/sample_po.pdf",
#         "doc_type": "purchase_order",
#         "po_number": "PO-1001",
#         "vendor": "AI Model Optimization",
#         "company": "OpenAI",
#         "item": "GPU Cluster",
#         "quantity": 5,
#         "amount": 4620
#     }

#     result = workflow.invoke(state)

#     print("PO RESULT")
#     print(result)

def test_po():

    state = {

        "document_type": "purchase_order",

        "ocr_text": """
        PURCHASE ORDER

        PO Number: PO-1001
        Vendor: AI Model Optimization
        Company: OpenAI
        Item: GPU Cluster
        Quantity: 5
        Amount: 4620
        """,

        "vendor": "AI Model Optimization",
        "company": "OpenAI",
        "po_number": "PO-1001",
        "amount": "4620"
    }

    result = workflow.invoke(state)

    print(result)
    
def test_invoice():

    state = {

        "document_type": "invoice",

        "ocr_text": """
        INVOICE

        Invoice Number: INV-1001
        PO Number: PO-1001
        Vendor: AI Model Optimization
        Company: OpenAI
        Amount: 4620
        """,

        "invoice_number": "INV-1001",
        "po_number": "PO-1001",
        "vendor": "AI Model Optimization",
        "company": "OpenAI",
        "amount": 4620
    }

    result = workflow.invoke(state)

    print("\nINVOICE RESULT")
    print(result)
    
def test_receipt():

    state = {

        "document_type": "receipt",

        "ocr_text": """
        RECEIPT

        Receipt Number: RC-1001
        Invoice Number: INV-1001
        Amount Paid: 4620
        Payment Date: 2026-03-12
        """,

        "receipt_number": "RC-1001",
        "invoice_number": "INV-1001",
        "amount_paid": 4620,
        "payment_date": "2026-03-12"
    }

    result = workflow.invoke(state)

    print("\nRECEIPT RESULT")
    print(result)


if __name__ == "__main__":

    print("\n--- TESTING PO WORKFLOW ---")
    test_po()

    print("\n--- TESTING INVOICE WORKFLOW ---")
    test_invoice()

    print("\n--- TESTING RECEIPT WORKFLOW ---")
    test_receipt()