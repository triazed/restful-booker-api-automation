from config.urls import Urls


class BookingClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def create_booking(self, create_payload):
        return self.session.post(f"{self.base_url}{Urls.BOOKING_URL}", json=create_payload)

    def get_booking_ids(self):
        return self.session.get(f"{self.base_url}{Urls.BOOKING_URL}")

    def get_booking(self, booking_id):
        return self.session.get(f"{self.base_url}{Urls.BOOKING_URL}/{booking_id}")

    def update_booking(self, booking_id, update_payload):
        return self.session.put(f"{self.base_url}{Urls.BOOKING_URL}/{booking_id}", json=update_payload)

    def partial_update_booking(self, booking_id, partial_update_payload):
        return self.session.patch(f"{self.base_url}{Urls.BOOKING_URL}/{booking_id}", json=partial_update_payload)

    def delete_booking(self, booking_id):
        return self.session.delete(f"{self.base_url}{Urls.BOOKING_URL}/{booking_id}")
