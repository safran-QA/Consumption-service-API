import pytest
from api.moderate_notifications_api import get_moderate_notifications


@pytest.mark.moderate_notifications
def test_moderate_notifications_valid(auth_token):
    response = get_moderate_notifications(auth_token)
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "success"
    assert isinstance(body["data"], list)
    assert "requestId" in body

    for item in body["data"]:
        assert "aircraft_type" in item
        assert "device_location" in item
        assert "device_name" in item
        assert "device_pn" in item
        assert "device_sn" in item
        assert "device_type" in item
        assert "errors" in item
        assert "iotec_aircraft_msn" in item


@pytest.mark.moderate_notifications
def test_moderate_notifications_empty_body(auth_token):
    response = get_moderate_notifications(auth_token, {})
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.moderate_notifications
def test_moderate_notifications_extra_field(auth_token):
    response = get_moderate_notifications(
        auth_token,
        {"unexpected_field": "test"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.moderate_notifications
def test_moderate_failure_information(auth_token):
    response = get_moderate_notifications(auth_token)
    assert response.status_code == 200

    for item in response.json()["data"]:
        for error in item["errors"]:
            assert "failure_information_text" in error


@pytest.mark.moderate_notifications
def test_moderate_repeat_count(auth_token):
    response = get_moderate_notifications(auth_token)
    assert response.status_code == 200

    for item in response.json()["data"]:
        for error in item["errors"]:
            if "repeat_count" in error:
                assert isinstance(error["repeat_count"], (int, float))


@pytest.mark.moderate_notifications
def test_moderate_device_information(auth_token):
    response = get_moderate_notifications(auth_token)
    assert response.status_code == 200

    for item in response.json()["data"]:
        assert item["device_pn"]
        assert item["device_sn"]
        assert item["device_name"]
        assert item["device_type"]
