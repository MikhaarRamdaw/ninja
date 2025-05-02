from fastapi import APIRouter, Query
from typing import Dict

router = APIRouter()

@router.get("/recon")
def passive_recon(target: str = Query(..., description="Target domain or IP")) -> Dict:
    # Dummy output to simulate passive recon
    return {
        "target": target,
        "status": "success",
        "data": {
            "ip_address": "192.168.1.1",
            "open_ports": [80, 443],
            "technologies": ["nginx", "react"],
            "whois": "Some WHOIS info here"
        }
    }
