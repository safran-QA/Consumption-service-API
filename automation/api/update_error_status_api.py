import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def update_error_status(
    token,
    device_pn,
    device_sn,
    failure_code,
    failure_status,
):
    return requests.post(
        f"{BASE_URL}/consumption/updateerrorstatus",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json={
            "device_pn": device_pn,
            "device_sn": device_sn,
            "failure_code": failure_code,
            "failure_status": failure_status,
        },
        timeout=30,
    )
