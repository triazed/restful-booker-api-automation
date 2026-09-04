# Restful Booker API Automation

API test automation project built with Python, pytest, and requests.

The project demonstrates automated REST API testing with reusable API clients,
pytest fixtures, test data management, authentication, response validation,
negative testing, and test data cleanup.

---

### API Under Test

- Restful Booker API: https://restful-booker.herokuapp.com/apidoc/index.html

---

### Tech Stack

- Python
- pytest
- requests

---

### Project Structure

- `clients/` – reusable API clients for authentication and booking endpoints
- `config/` – base URL and API endpoint configuration
- `test_data/` – reusable test payloads and credentials
- `tests/` – API test scenarios
- `conftest.py` – shared pytest fixtures, sessions, authentication, and test setup/cleanup

---

### Test Coverage

The project covers:

- **Health Check**
  - Verify API availability (`GET /ping`)

- **Authentication**
  - Create an authentication token with valid credentials
  - Verify authentication behavior with invalid credentials

- **Booking**
  - Get booking IDs
  - Get booking by ID
  - Create booking
  - Full booking update (`PUT`)
  - Partial booking update (`PATCH`)
  - Delete booking
  - Verify persisted data after update operations
  - Validate behavior for invalid booking IDs
  - Validate unauthorized and invalid-token requests
  - Validate invalid and incomplete request payloads

---

### Known API Validation Issues
During testing, several validation inconsistencies were identified in the API.

Some booking fields accept values with unexpected data types instead of rejecting
the request. Tests covering these known issues are marked with pytest.mark.xfail
to document the current behavior without treating known API defects as unexpected
test-suite failures.

---

### Design Notes
* API interaction is encapsulated in reusable client classes.
* Authenticated and unauthenticated requests use separate requests.Session instances.
* Shared setup and authentication logic is implemented with pytest fixtures.
* Tests create dynamic booking data where resource-specific scenarios require it.
* Created test resources are cleaned up after execution where applicable.
* Test data is separated from test logic.
* Parameterization is used for equivalent negative scenarios.
* Known API defects are explicitly documented rather than hidden from the test suite.

---

### Install Dependencies

```bash
pip install -r requirements.txt
---
### Run tests
- pytest
---
### Notes
- Tests are independent and create their own data 
- Test data is separated from test logic
- Authentication is handled via pytest fixture
- Project is intentionally kept simple and focused