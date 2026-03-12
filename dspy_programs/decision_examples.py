import dspy

trainset = [

    dspy.Example(
        vendor="ABC Ltd",
        total="$540",
        fraud_score="10",
        fraud_reason="Normal vendor",
        decision="approve",
        explanation="Low risk invoice"
    ).with_inputs("vendor","total","fraud_score","fraud_reason"),

    dspy.Example(
        vendor="Unknown Vendor",
        total="$12000",
        fraud_score="82",
        fraud_reason="High invoice amount",
        decision="manual_review",
        explanation="Large invoice requires review"
    ).with_inputs("vendor","total","fraud_score","fraud_reason")

]