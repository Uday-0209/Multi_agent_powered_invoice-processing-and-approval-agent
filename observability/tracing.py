import os
from langsmith import traceable

@traceable

def trace_agent(agent_name: str, payload: dict):
    print(f"Tracing {agent_name}")
    return payload 