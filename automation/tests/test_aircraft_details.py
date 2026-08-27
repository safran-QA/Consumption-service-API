import os

import pytest
from dotenv import load_dotenv

from api.aircraft_api import get_aircraft_details

load_dotenv()

TEST_AIRCRAFT_ID = os.getenv("TEST_AIRCRAFT_ID", "331")


@pytest.mark.aircraft
def test_aircraft_details_valid(auth_token):
    """
    AIR-001
    Verify aircraft details can be retrieved using a valid aircraft ID.
    """

    response = get_aircraft_details(
        auth_token,
        TEST_AIRCRAFT_ID
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
    assert "message" in body
    assert "requestId" in body

    data = body["data"]

    assert data["aircraft_id"] == TEST_AIRCRAFT_ID
    assert "aircraft_body" in data
    assert "aircraft_manufacturing_date" in data
    assert "aircraft_tailnumber" in data
    assert "aircraft_type" in data
    assert "airline_name" in data
    assert "devices" in data

    assert isinstance(data["devices"], list)
