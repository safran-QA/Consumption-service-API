import pytest

from api.aircraft_status_api import get_aircraft_status


@pytest.mark.aircraft_status
def test_aircraft_status_valid(auth_token):
    """STAT-AC-P01"""
    response = get_aircraft_status(auth_token)

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert "data" in body
    assert isinstance(body["data"], list)
    assert "requestId" in body


@pytest.mark.aircraft_status
def test_aircraft_status_aircraft_id(auth_token):
    """ADD-010"""
    response = get_aircraft_status(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for aircraft in data:
        assert "aircraft_id" in aircraft


@pytest.mark.aircraft_status
def test_aircraft_status_aircraft_status(auth_token):
    """ADD-011"""
    response = get_aircraft_status(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for aircraft in data:
        assert "aircraft_status" in aircraft


@pytest.mark.aircraft_status
def test_aircraft_status_aircraft_type(auth_token):
    """ADD-012"""
    response = get_aircraft_status(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for aircraft in data:
        assert "aircraft_type" in aircraft


@pytest.mark.aircraft_status
def test_aircraft_status_err_devices(auth_token):
    """ADD-013"""
    response = get_aircraft_status(auth_token)

    assert response.status_code == 200

    data = response.json()["data"]

    for aircraft in data:
        assert "err_devices" in aircraft
