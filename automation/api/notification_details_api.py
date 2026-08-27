import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def get_notification_details(
    token,
    device_pn,
    device_sn,
    failure_code,
):
    return requests.post(
        f"{BASE_URL}/consumption/notificationdetails/applyfilter",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json={
            "device_pn": device_pn,
            "device_sn": device_sn,
            "failure_code": failure_code,
        },
        timeout=30,
    )
