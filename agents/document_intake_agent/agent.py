# import uuid
# from utils.event_logger import log_event


# class DocumentIntakeAgent:

#     def run(self, state: dict):

#         print("Running Document Intake Agent")

#         if "workflow_id" not in state:
#             state["workflow_id"] = str(uuid.uuid4())

#         file_path = state["file_path"]

#         state.setdefault("events", []).append({
#             "agent": "document_intake",
#             "workflow_id": state["workflow_id"],
#             "file_path": file_path
#         })

#         if not file_path.endswith(".pdf"):
#             raise ValueError("only pdf files are supported")

#         output = {"document_status": "intake_completed"}

#         log_event(
#             state,
#             "document_intake",
#             output
#         )

#         return output

from utils.event_logger import log_event


class DocumentIntakeAgent:

    def run(self, state):

        print("Running Document Intake Agent")

        file_path = state.get("file_path")

        # TEST MODE: no file upload
        if not file_path:

            log_event(
                state,
                "document_intake",
                {"mode": "test"}
            )

            return {}

        # PRODUCTION MODE
        log_event(
            state,
            "document_intake",
            {"file_path": file_path}
        )

        return {}