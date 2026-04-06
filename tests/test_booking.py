import requests
from copy import deepcopy
from config import urls
from test_data import booking_data


class TestBooking:

    def test_get_booking_returns_booking_ids(self):
        response = requests.get(urls.BOOKING_URL)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_booking_by_id_returns_booking_details(self):
        response = requests.get(urls.BOOKING_URL)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) > 0
        booking_id = data[0]["bookingid"]
        response = requests.get(f"{urls.BOOKING_URL}/{booking_id}")
        data = response.json()
        assert response.status_code == 200
        assert "firstname" in data
        assert "lastname" in data
        assert "totalprice" in data

    def test_create_booking_returns_booking_id_and_data(self):
        booking = booking_data.booking_data
        response = requests.post(urls.BOOKING_URL, json=booking)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data["bookingid"], int)
        assert booking == data["booking"]

    def test_patch_booking_updates_booking_data(self, admin_token):
        booking = deepcopy(booking_data.booking_data)
        response = requests.post(urls.BOOKING_URL, json=booking)
        data = response.json()
        assert response.status_code == 200
        assert booking == data["booking"]
        booking_id = data["bookingid"]

        patch_booking_data = booking_data.patch_booking_data
        booking.update(patch_booking_data)

        headers = {
            "Cookie": f"token={admin_token}"
        }
        response = requests.patch(f"{urls.BOOKING_URL}/{booking_id}", json=patch_booking_data,
                                  headers=headers)

        data = response.json()
        assert response.status_code == 200
        assert booking == data

    def test_delete_booking_removes_created_booking(self, admin_token):

        booking = booking_data.booking_data

        response = requests.post(urls.BOOKING_URL, json=booking)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data["bookingid"], int)
        assert booking == data["booking"]
        booking_id = data["bookingid"]

        headers = {
            "Cookie": f"token={admin_token}"
        }
        response = requests.delete(f"{urls.BOOKING_URL}/{booking_id}", headers=headers)
        assert response.status_code == 201

        response = requests.get(f"{urls.BOOKING_URL}/{booking_id}")
        assert response.status_code == 404
