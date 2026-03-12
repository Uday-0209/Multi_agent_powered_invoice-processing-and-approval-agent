from orchestration.workflow import build_workflow

workflow = build_workflow()


def test_purchase_order():

    state = {
        "file_path": "tests/sample_po.pdf",

        "document_type": "purchase_order",

        "po_number": "PO1001",

        "vendor": "ABC Ltd",
        "company": "XYZ Corp",

        "item": "Steel Rod",
        "quantity": 200,

        "amount": 5000,

        "invoice_number": None,
        "receipt_number": None,

        "amount_paid": None
    }

    result = workflow.invoke(state)

    print("\nFINAL RESULT\n")
    print(result)


if __name__ == "__main__":
    test_purchase_order()