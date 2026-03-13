from datetime import datetime

def log_event(state, agent_name, data=None):

    event = {
        "agent": agent_name,
        "timestamp": datetime.utcnow().isoformat()
    }

    if data:
        event["data"] = data

    state.setdefault("events", []).append(event)

    return state