import pytest
from config.urls import Urls
from test_data.booking_data import booking_data, invalid_booking_data, full_update_booking_data, invalid_full_update_booking_data, known_validation_issues, invalid_booking_ids


class TestBooking:

    def test_get_booking_ids_returns_booking_ids(self, unauthorized_booking_client):
        response = unauthorized_booking_client.get_booking_ids()
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert data
        for item in data:
            assert isinstance(item, dict)
            assert item
            assert "bookingid" in item
            assert isinstance(item["bookingid"], int)
            assert item["bookingid"] > 0

    def test_get_booking_by_id_returns_booking_data(self, unauthorized_booking_client, created_booking):
        booking_id = created_booking["booking_id"]
        loaded_booking_data = created_booking["loaded_booking_data"]

        response = unauthorized_booking_client.get_booking(booking_id)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert data
        assert data == loaded_booking_data

    @pytest.mark.parametrize("booking_id", invalid_booking_ids)
    def test_get_booking_by_invalid_id_returns_error(self, unauthorized_booking_client, booking_id):
        response = unauthorized_booking_client.get_booking(booking_id)

        assert response.status_code == 404
        assert response.text == "Not Found"

    def test_create_booking_valid_booking_data_returns_booking_id_and_data(self, unauthorized_booking_client, authorized_booking_client):
        response = unauthorized_booking_client.create_booking(booking_data)
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, dict)
        assert data
        assert "bookingid" in data
        assert isinstance(data["bookingid"], int)
        assert data["bookingid"] > 0
        assert "booking" in data
        assert isinstance(data["booking"], dict)
        assert data["booking"] == booking_data

        delete_response = authorized_booking_client.delete_booking(data["bookingid"])
        assert delete_response.status_code == 201

    @pytest.mark.parametrize("invalid_booking_data", invalid_booking_data)
    def test_create_booking_invalid_booking_data_returns_error(self, unauthorized_booking_client, invalid_booking_data):
        response = unauthorized_booking_client.create_booking(invalid_booking_data)
        assert response.status_code == 500
        assert response.text == "Internal Server Error"

    @pytest.mark.parametrize("invalid_booking_data", known_validation_issues)
    def test_create_booking_with_invalid_field_types_returns_error(self, unauthorized_booking_client, invalid_booking_data):
        response = unauthorized_booking_client.create_booking(invalid_booking_data)

        assert response.status_code >= 400

    def test_update_booking_updates_booking(self, authorized_booking_client, unauthorized_booking_client, created_booking):
        booking_id = created_booking["booking_id"]

        updated_response = authorized_booking_client.update_booking(booking_id, full_update_booking_data)
        assert updated_response.status_code == 200

        updated_data = updated_response.json()
        assert isinstance(updated_data, dict)
        assert updated_data
        assert updated_data == full_update_booking_data

        check_booking_response = unauthorized_booking_client.get_booking(booking_id)
        assert check_booking_response.status_code == 200

        checked_data = check_booking_response.json()
        assert isinstance(checked_data, dict)
        assert checked_data
        assert checked_data == full_update_booking_data

    def test_update_booking_unauthorized_returns_error(self, unauthorized_booking_client, created_booking):
        booking_id = created_booking["booking_id"]

        updated_response = unauthorized_booking_client.update_booking(booking_id, full_update_booking_data)
        assert updated_response.status_code == 403
        assert updated_response.text == "Forbidden"

    def test_update_booking_incorrect_token_returns_error(self, unauthorized_session, created_booking):
        booking_id = created_booking["booking_id"]

        headers = {
            "Cookie": "token=abc"
        }

        updated_response = unauthorized_session.put(f"{Urls.BASE_URL}{Urls.BOOKING_URL}/{booking_id}", json=full_update_booking_data, headers=headers)
        assert updated_response.status_code == 403
        assert updated_response.text == "Forbidden"

    @pytest.mark.parametrize("booking_id", invalid_booking_ids)
    def test_update_booking_invalid_booking_id_returns_error(self, authorized_booking_client, booking_id):
        updated_response = authorized_booking_client.update_booking(booking_id, full_update_booking_data)
        assert updated_response.status_code == 405
        assert updated_response.text == "Method Not Allowed"

    def test_update_booking_empty_payload_returns_error(self, authorized_booking_client, created_booking):
        booking_id = created_booking["booking_id"]
        update_booking_data = {}

        updated_response = authorized_booking_client.update_booking(booking_id, update_booking_data)
        assert updated_response.status_code == 400
        assert updated_response.text == "Bad Request"

    def test_update_booking_missing_required_field_returns_error(self, authorized_booking_client, created_booking):
        booking_id = created_booking["booking_id"]

        updated_response = authorized_booking_client.update_booking(booking_id, invalid_full_update_booking_data)
        assert updated_response.status_code == 400
        assert updated_response.text == "Bad Request"

