from config.urls import Urls


class TestPing:

    def test_ping_returns_created_status(self, unauthorized_session):
        response = unauthorized_session.get(f"{Urls.BASE_URL}{Urls.PING_URL}")
        assert response.status_code == 201
