from config.urls import Urls


class AuthClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def create_token(self, auth_credentials_payload):
        return self.session.post(f"{self.base_url}{Urls.AUTH_URL}", json=auth_credentials_payload)
