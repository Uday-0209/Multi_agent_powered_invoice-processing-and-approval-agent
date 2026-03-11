from fastapi import APIRouter

router =  APIRouter(prefix="/agents", tags = ["agents"])

@router.get('/')

def list_agents():
    return {
        "agents":[
            "ocr_agent",
            "classification_agent",
            "extraction_agent",
            "vendor_verification_agent",
            "validation_agent",
            "fraud_agent",
            "policy_agent",
            "decision_agent",
            "audit_agent"
        ]
    }