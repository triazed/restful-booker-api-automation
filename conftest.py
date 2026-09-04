import pytest
import requests
from requests import Session
from test_data import auth_credentials
from config import urls
from clients.auth_client import AuthClient
from clients.booking_client import BookingClient
from config.urls import Urls
from test_data.auth_credentials import AuthCredentials


@pytest.fixture()
def unauthorized_session():
    session = Session()
    session.headers.update(
        {
            "Accept": "application/json",
        }
    )
    yield session
    session.close()

@pytest.fixture()
def authorized_session(auth_token):
    session = Session()
    session.headers.update(
        {
            "Accept": "application/json",
            "Cookie": f"token={auth_token}"
        }
    )
    yield session
    session.close()

@pytest.fixture()
def auth_token(auth_client):
    response = auth_client.create_token(AuthCredentials.admin_credentials)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data != {}
    assert "token" in data
    assert isinstance(data["token"], str)
    assert data["token"] != ""

    yield data["token"]

@pytest.fixture()
def auth_client(unauthorized_session):
    return AuthClient(Urls.BASE_URL, unauthorized_session)

@pytest.fixture()
def authorized_booking_client(authorized_session):
    return BookingClient(Urls.BASE_URL, authorized_session)

@pytest.fixture()
def unauthorized_booking_client(unauthorized_session):
    return BookingClient(Urls.BASE_URL, unauthorized_session)

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
