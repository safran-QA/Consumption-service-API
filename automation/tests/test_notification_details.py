import pytest
from api.notification_details_api import get_notification_details


DEVICE_PN = "NUVO.SO.26"
DEVICE_SN = "180003"
FAILURE_CODE = "NUVO.SO.26_Phase_loss"


def notification(auth_token):
    return get_notification_details(
        auth_token,
        DEVICE_PN,
        DEVICE_SN,
        FAILURE_CODE,
    )


@pytest.mark.notification_details
def test_notification_details_valid(auth_token):
    response = notification(auth_token)
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "success"
    assert "data" in body
    assert "requestId" in body


@pytest.mark.notification_details
def test_notification_failure_name(auth_token):
    data = notification(auth_token).json()["data"]
    assert isinstance(data, dict)
    assert "errors" in data
    assert isinstance(data["errors"], list)
    assert len(data["errors"]) > 0
    assert "failure_name" in data["errors"][0]


@pytest.mark.notification_details
def test_notification_failure_type(auth_token):
    data = notification(auth_token).json()["data"]
    assert isinstance(data, dict)
    assert "errors" in data
    assert isinstance(data["errors"], list)
    assert len(data["errors"]) > 0
    assert "failure_type" in data["errors"][0]


@pytest.mark.notification_details
def test_notification_inspection_instructions(auth_token):
    data = notification(auth_token).json()["data"]
    assert isinstance(data, dict)
    assert "errors" in data
    assert isinstance(data["errors"], list)
    assert len(data["errors"]) > 0
    assert "inspection_instructions" in data["errors"][0]


@pytest.mark.notification_details
def test_notification_repair_instructions(auth_token):
    data = notification(auth_token).json()["data"]
    assert isinstance(data, dict)
    assert "errors" in data
    assert isinstance(data["errors"], list)
    assert len(data["errors"]) > 0
    assert "repair_instructions" in data["errors"][0]
