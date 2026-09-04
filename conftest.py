import pytest
from requests import Session
from clients.auth_client import AuthClient
from clients.booking_client import BookingClient
from config.urls import Urls
from test_data.auth_credentials import AuthCredentials
from test_data.booking_data import booking_data


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
    assert data["token"]

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

@pytest.fixture()
def created_booking(unauthorized_booking_client, authorized_booking_client):
    response = unauthorized_booking_client.create_booking(booking_data)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data
    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)
    assert "booking" in data
    assert isinstance(data["booking"], dict)
    assert data["booking"]

    yield {
        "booking_id": data["bookingid"],
        "loaded_booking_data": booking_data,
        "created_booking_data": data["booking"]
    }
    authorized_booking_client.delete_booking(data["bookingid"])

