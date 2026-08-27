import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def get_moderate_notifications(token, payload=None):
    return requests.post(
        f"{BASE_URL}/consumption/nmoderate/applyfilter",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json=payload if payload is not None else {},
        timeout=30,
    )
