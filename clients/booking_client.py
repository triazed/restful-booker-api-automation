class BookingClient:
    def __init__(self, url, session):
        self.url = url
        self.session = session

    def create_booking(self, create_payload):
        return self.session.post(self.url, json=create_payload)

    def get_booking_ids(self):
        return self.session.get(self.url)

    def get_booking(self, booking_id):
        return self.session.get(f"{self.url}/{booking_id}")

    def update_booking(self, booking_id, update_payload):
        return self.session.put(f"{self.url}/{booking_id}", json=update_payload)

    def partial_update_booking(self, booking_id, partial_update_payload):
        return self.session.patch(f"{self.url}/{booking_id}", json=partial_update_payload)

    def delete_booking(self, booking_id):
        return self.session.delete(f"{self.url}/{booking_id}")
