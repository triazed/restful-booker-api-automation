import pytest
import requests
from test_data import auth_credentials
from config import urls


@pytest.fixture
def admin_token():
    admin_credentials = auth_credentials.admin_credentials
    response = requests.post(urls.AUTH_URL, json=admin_credentials)
    data = response.json()
    assert response.status_code == 200
    assert "token" in data
    assert isinstance(data["token"], str)
    assert data["token"]
    return data["token"]
