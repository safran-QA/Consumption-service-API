import os

import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_URL = os.getenv("AUTH_URL")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")


def test_login_success():
    response = requests.post(
        f"{AUTH_URL}/users/login",
        json={
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD,
        },
        timeout=30,
    )

    print("\nHTTP STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert body["data"]["AccessToken"]
    assert body["data"]["TokenType"] == "Bearer"
