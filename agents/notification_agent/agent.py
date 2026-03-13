from tools.notification_tools import NotificationTools
from dotenv import load_dotenv
import os
from langsmith import traceable

load_dotenv()

@traceable(name = "NotificationAgent")
class NotificationAgent:
    def __init__(self) -> None:
        self.notify = NotificationTools()
        
    def run(self, state: dict):
        message = {
            "document_type": state.get("document_type"),
            "company": state.get("company"),
            "vendor": state.get("vendor"),
            "amount": state.get("amount"),
            "decision": state.get("decision")
        }
        
        self.notify.send_notification(message)
        
        return state