import os

import pytest
from dotenv import load_dotenv

from api.aircraft_api import get_aircraft_details

load_dotenv()


@pytest.mark.aircraft
def test_aircraft_details_valid(auth_token):
    """
    AIR-001
    Verify aircraft details API returns a successful response
    for a valid aircraft ID.
    """

    aircraft_id = os.getenv("TEST_AIRCRAFT_ID")

    assert aircraft_id, (
        "TEST_AIRCRAFT_ID is not configured in .env"
    )

    response = get_aircraft_details(
        auth_token,
        aircraft_id,
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
    assert "message" in body
    assert "requestId" in body
