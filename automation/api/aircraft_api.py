import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_aircraft_details(token, aircraft_id):
    url = f"{BASE_URL}/consumption/aircraftdetails/applyfilter"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "aircraft_id": aircraft_id
    }

    return requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )
