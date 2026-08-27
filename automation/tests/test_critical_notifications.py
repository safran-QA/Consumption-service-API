import pytest

from api.critical_notifications_api import get_critical_notifications


@pytest.mark.critical_notifications
def test_critical_notifications_valid(auth_token):
    """NOTIF-CRIT-P01"""
    response = get_critical_notifications(auth_token)

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
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


@pytest.mark.critical_notifications
def test_critical_notifications_empty_result(auth_token):
    """NOTIF-CRIT-E01"""
    response = get_critical_notifications(auth_token)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert isinstance(body["data"], list)


@pytest.mark.critical_notifications
def test_critical_notifications_extra_field(auth_token):
    """NOTIF-CRIT-E02"""
    response = get_critical_notifications(
        auth_token,
        {"unexpected_field": "test"},
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body


@pytest.mark.critical_notifications
def test_critical_notification_failure_code(auth_token):
    """ADD-022"""
    response = get_critical_notifications(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for item in data:
        for error in item["errors"]:
            assert "failure_code" in error


@pytest.mark.critical_notifications
def test_critical_notification_device_information(auth_token):
    """ADD-023"""
    response = get_critical_notifications(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for item in data:
        assert item["device_pn"]
        assert item["device_sn"]
        assert item["device_name"]
        assert item["device_type"]


@pytest.mark.critical_notifications
def test_critical_notification_time_of_failure(auth_token):
    """ADD-024"""
    response = get_critical_notifications(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for item in data:
        for error in item["errors"]:
            assert "time_of_failure" in error
