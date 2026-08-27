import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_device_status(token):
    url = f"{BASE_URL}/consumption/devicestatus/applyfilter"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    return requests.post(
        url,
        headers=headers,
        json={},
        timeout=30,
    )
