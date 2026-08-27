import pytest
from api.update_error_status_api import update_error_status


DEVICE_PN = "NUVO.SO.26"
DEVICE_SN = "180003"
FAILURE_CODE = "NUVO.SO.26_Phase_loss"


@pytest.mark.update_error_status
def test_update_error_status_valid(auth_token):
    response = update_error_status(
        auth_token,
        DEVICE_PN,
        DEVICE_SN,
        FAILURE_CODE,
        "New",
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "success"
    assert "requestId" in body
