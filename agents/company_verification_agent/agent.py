from utils.event_logger import log_event
from dotenv import load_dotenv
import os
from langsmith import traceable
load_dotenv()

@traceable(name = "CompanyVerificationAgent")
class CompanyVerificationAgent:
    def __init__(self):
        pass

    def run(self, state: dict):
        # Placeholder for company verification logic
        print("Running company verification...")

        # Simulate verification result
        verification_result = {
            "company_verified": True,
            "company_name": "Example Corp"
        }

        # state = {
        #     **state,
        #     **verification_result
        # }

        log_event(
            state,
            "company_verification",
            verification_result
        )

        return verification_result