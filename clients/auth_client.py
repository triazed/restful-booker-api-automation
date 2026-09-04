class AuthClient:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    def create_token(self, auth_credentials_payload):
        return self.session.post(self.url, json=auth_credentials_payload)
