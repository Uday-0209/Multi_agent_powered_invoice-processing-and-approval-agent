from tools.notification_tools import NotificationTools

class NotificationAgent:
    def __init__(self) -> None:
        self.notify = NotificationTools()
        
    def run(self, state: dict):
        message = {
            "document_type": state["document_type"],
            "company": state["company"],
            "vendor": state["vendor"],
            "amount": state["amount"],
            "decision": state["decision"]
        }
        
        self.notify.send_notification(message)
        
        return state