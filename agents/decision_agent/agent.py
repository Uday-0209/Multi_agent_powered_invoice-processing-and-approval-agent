class DecisionAgent:

    def run(self, fraud_score: int):

        if fraud_score < 30:
            decision = "approved"

        elif fraud_score < 70:
            decision = "manual_review"

        else:
            decision = "rejected"

        return {"decision": decision}