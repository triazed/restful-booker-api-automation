import requests
from config import urls
from test_data import auth_credentials


class TestAuth:

    def test_create_token_returns_token(self):
        admin_credentials = auth_credentials.admin_credentials
        response = requests.post(urls.AUTH_URL, json=admin_credentials)
        data = response.json()
        assert response.status_code == 200
        assert "token" in data
        assert isinstance(data["token"], str)
        assert data["token"]
