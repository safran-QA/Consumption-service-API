import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_device_details(token, device_pn, device_sn):
    url = f"{BASE_URL}/consumption/devicedetails/applyfilter"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    return requests.post(
        url,
        headers=headers,
        json={
            "device_pn": device_pn,
            "device_sn": device_sn,
        },
        timeout=30,
    )
