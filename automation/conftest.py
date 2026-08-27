import os

import pytest
import requests
from dotenv import load_dotenv

from utils.test_data import save_data, DATA_FILE

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
AUTH_URL = os.getenv("AUTH_URL")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")


@pytest.fixture(scope="session", autouse=True)
def auth_token():
    """Authenticate once and store runtime authentication data."""

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

    assert body["status"] == "success"

    token = body["data"]["AccessToken"]

    save_data("access_token", token)
    save_data("token_type", body["data"]["TokenType"])

    print("\nRuntime authentication data created.")
    print("Token stored in:", DATA_FILE)

    return token


@pytest.fixture(scope="session", autouse=True)
def cleanup_test_data():
    yield

    if DATA_FILE.exists():
        DATA_FILE.unlink()
        print("\nRuntime test data deleted.")
