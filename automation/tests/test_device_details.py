import pytest

from api.device_details_api import get_device_details


DEVICE_PN = "NUVO.SO.26"
DEVICE_SN = "180003"


@pytest.mark.device_details
def test_device_details_valid(auth_token):
    """AD-DEVICE-P01"""
    response = get_device_details(
        auth_token,
        DEVICE_PN,
        DEVICE_SN,
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
    assert "requestId" in body


@pytest.mark.device_details
def test_device_details_software_version(auth_token):
    """ADD-020"""
    response = get_device_details(
        auth_token,
        DEVICE_PN,
        DEVICE_SN,
    )

    assert response.status_code == 200

    data = response.json()["data"]

    assert isinstance(data, list)
    assert len(data) > 0
    assert "device_software_version" in data[0]



@pytest.mark.device_details
def test_device_details_errors(auth_token):
    """ADD-021"""
    response = get_device_details(
        auth_token,
        DEVICE_PN,
        DEVICE_SN,
    )

    assert response.status_code == 200

    data = response.json()["data"]

    assert isinstance(data, list)
    assert len(data) > 0
    assert "errors" in data[0]

