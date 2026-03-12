class HumanReviewAgent:

    def run(self, state):

        return {
            **state,
            "status": "waiting_for_human_review"
        }