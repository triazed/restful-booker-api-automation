from test_data.auth_credentials import AuthCredentials
import pytest


class TestAuth:

    def test_create_token_with_valid_credentials_returns_token(self, auth_client):
        response = auth_client.create_token(AuthCredentials.admin_credentials)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert data
        assert "token" in data
        assert isinstance(data["token"], str)
        assert data["token"]

    @pytest.mark.parametrize("invalid_credentials", AuthCredentials.invalid_admin_credentials)
    def test_create_token_invalid_credentials_returns_error(self, auth_client, invalid_credentials):
        response = auth_client.create_token(invalid_credentials)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert data
        assert data["reason"] == "Bad credentials"
        assert "token" not in data

