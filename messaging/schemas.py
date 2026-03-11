from pydantic import BaseModel
from typing import Dict


class AgentMessage(BaseModel):
    task_id: str
    from_agent: str
    to_agent: str
    task_type: str
    payload: Dict