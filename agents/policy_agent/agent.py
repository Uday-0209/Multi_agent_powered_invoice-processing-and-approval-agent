from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "PolicyAgent")
class PolicyAgent:

    def run(self, state):

        raw_total = state.get("total", "0")

        clean_total = (
            str(raw_total)
            .replace("$", "")
            .replace(",", "")
            .strip()
        )

        total = float(clean_total)

        if total > 10000:

            result = {
                "policy_flag": True,
                "policy_reason": "Amount exceeds approval threshold"
            }

        else:

            result = {
                "policy_flag": False,
                "policy_reason": ""
            }

        log_event(
            state,
            "policy_evaluation",
            result
        )

        return result