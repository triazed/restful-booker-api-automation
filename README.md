# Restful Booker API Automation
API test automation project built with Python, pytest, and requests.
The project demonstrates automated API testing, including working with REST endpoints, request/response validation, and test structuring.
---
### API Under Test
- https://restful-booker.herokuapp.com/apidoc/index.html
---
### Tech stack
- Python
- Pytest
- Requests
---
### Project structure
- tests/ – test scenarios
- test_data/ – test data
- config/ – API endpoints
---
### Test coverage
The project covers:
- Health Check. Verify API availability (`/ping`)
- Authentication. Create admin token (`/auth`)
- Booking (Get booking IDs, Get booking by ID, Create booking, Update booking (PATCH), Delete booking)
---
### Install dependencies
- pip install -r requirements.txt
---
### Run tests
- pytest
---
### Notes
- Tests are independent and create their own data 
- Test data is separated from test logic
- Authentication is handled via pytest fixture
- Project is intentionally kept simple and focused