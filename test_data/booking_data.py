import pytest


booking_data = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-01-01",
        "checkout": "2027-01-01"
    },
    "additionalneeds": "Breakfast"
}

invalid_booking_data = [
    # wrong firstname type
    {
        "firstname": 222,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # wrong lastname type
    {
        "firstname": "Jim",
        "lastname": 222,
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # missing firstname
    {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # missing lastname
    {
        "firstname": "Jim",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # missing totalprice
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # missing depositpaid
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2027-01-01"
        },
        "additionalneeds": "Breakfast"
    },

    # missing bookingdates
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "additionalneeds": "Breakfast"
    },
]

known_validation_issues = [
    pytest.param(
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": True,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": "2027-01-01"
            },
            "additionalneeds": "Breakfast"
        },
        marks=pytest.mark.xfail(
            reason="Known API issue: totalprice accepts boolean values",
            strict=True
        ),
        id="totalprice_boolean"
    ),

    pytest.param(
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": "True",
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": "2027-01-01"
            },
            "additionalneeds": "Breakfast"
        },
        marks=pytest.mark.xfail(
            reason="Known API issue: depositpaid accepts string values",
            strict=True
        ),
        id="depositpaid_string"
    ),

    pytest.param(
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": 111,
                "checkout": "2027-01-01"
            },
            "additionalneeds": "Breakfast"
        },
        marks=pytest.mark.xfail(
            reason="Known API issue: checkin accepts non-string values",
            strict=True
        ),
        id="checkin_integer"
    ),

    pytest.param(
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": 222
            },
            "additionalneeds": "Breakfast"
        },
        marks=pytest.mark.xfail(
            reason="Known API issue: checkout accepts non-string values",
            strict=True
        ),
        id="checkout_integer"
    ),

    pytest.param(
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": "2027-01-01"
            },
            "additionalneeds": 444
        },
        marks=pytest.mark.xfail(
            reason="Known API issue: additionalneeds accepts non-string values",
            strict=True
        ),
        id="additionalneeds_integer"
    ),
]

partial_update_booking_data = {
    "firstname": "James",
    "totalprice": 333,
}

full_update_booking_data = {
    "firstname": "Charles",
    "lastname": "White",
    "totalprice": 555,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2026-06-06",
        "checkout": "2027-07-07"
    },
    "additionalneeds": "Dinner"
}

invalid_full_update_booking_data = {
    "lastname": "White",
    "totalprice": 555,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2026-06-06",
        "checkout": "2027-07-07"
    },
    "additionalneeds": "Dinner"
    }

invalid_booking_ids = [
    -1,
    0,
    "abc",
    None,
]
