import dspy

trainset = [

    dspy.Example(
        text="Invoice from ABC Ltd Total $540",
        vendor="ABC Ltd",
        total="$540"
    ).with_inputs("text"),

    dspy.Example(
        text="Vendor: XYZ Corp Amount Due: $1200",
        vendor="XYZ Corp",
        total="$1200"
    ).with_inputs("text")

]