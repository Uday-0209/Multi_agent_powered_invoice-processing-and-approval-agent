class PolicyAgent:

    def run(self, state):

        total = float(state["total"].replace("$", ""))

        if total > 10000:

            return {
                **state,
                "policy_flag": True,
                "policy_reason": "Amount exceeds approval threshold"
            }

        return {
            **state,
            "policy_flag": False
        }