import pytest
import requests
from utils import BASE_URL, get_headers

@pytest.fixture(scope="session")
def auth_token():
    res = requests.post(f"{BASE_URL}/api/auth", headers=get_headers())

    # Accept all valid responses
    assert res.status_code in [200, 201, 409]

    data = res.json()

    print("Auth Response:", data)  # for debugging

    return data.get("token")  # safely returns None if not present