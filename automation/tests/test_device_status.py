import pytest

from api.device_status_api import get_device_status
from utils.test_data import save_data


@pytest.mark.device
def test_device_status_and_capture_aircraft(auth_token):
    """
    DEV-001
    Verify device status API and capture aircraft ID
    for downstream API tests.
    """

    response = get_device_status(auth_token)

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
    assert isinstance(body["data"], list)

    assert len(body["data"]) > 0, (
        "Device Status API returned no device records."
    )

    device = body["data"][0]

    assert "iotec_aircraft_msn" in device

    aircraft_id = device["iotec_aircraft_msn"]

    assert aircraft_id

    save_data("aircraft_id", aircraft_id)

    print("\nAircraft ID captured:", aircraft_id)
