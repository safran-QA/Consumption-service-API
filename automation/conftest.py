import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
AUTH_URL = os.getenv("AUTH_URL")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")


@pytest.fixture(scope="session")
def auth_token():
    """Authenticate once and return the JWT access token."""

    response = requests.post(
        f"{AUTH_URL}/users/login",
        json={
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD,
        },
        timeout=30,
    )

    assert response.status_code == 200, (
        f"Login failed: HTTP {response.status_code}\n"
        f"Response: {response.text}"
    )

    body = response.json()

    token = body["data"]["AccessToken"]

    assert token, "AccessToken was empty"

    return token


@pytest.fixture
def auth_headers(auth_token):
    """Authorization headers for protected Consumption APIs."""

    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
