import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_critical_notifications(token, payload=None):
    url = f"{BASE_URL}/consumption/ncritical/applyfilter"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    return requests.post(
        url,
        headers=headers,
        json=payload if payload is not None else {},
        timeout=30,
    )
