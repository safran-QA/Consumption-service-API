import pytest


@pytest.mark.auth
def test_login_success(auth_token):
    """
    AUTH-001
    Verify user can successfully authenticate.
    """

    assert auth_token
    assert isinstance(auth_token, str)
    assert len(auth_token) > 0

    print("\nAUTH-001: Login successful")
    print("Access token generated successfully.")
