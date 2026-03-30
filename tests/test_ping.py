import requests
from config import urls


class TestPing:

    def test_ping_returns_created_status(self):
        response = requests.get(urls.PING_URL)
        assert response.status_code == 201
