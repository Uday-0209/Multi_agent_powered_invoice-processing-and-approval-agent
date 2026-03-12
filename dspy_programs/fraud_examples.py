import dspy

trainset = [

    dspy.Example(
        vendor="ABC Ltd",
        total="$540",
        invoice_number="INV-001",
        risk_score="10",
        reason="Small amount from normal vendor"
    ).with_inputs("vendor", "total", "invoice_number"),

    dspy.Example(
        vendor="Unknown Vendor",
        total="$12000",
        invoice_number="INV-002",
        risk_score="85",
        reason="Large amount from unknown vendor"
    ).with_inputs("vendor", "total", "invoice_number")

]