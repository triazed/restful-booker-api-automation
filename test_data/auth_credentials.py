class AuthCredentials:

    admin_credentials = {
        "username": "admin",
        "password": "password123"
    }

    invalid_admin_credentials = [
        {
            "username": "adm",
            "password": "password123"
        },
        {
            "username": "admin",
            "password": "pass"
        },
        {
            "username": "admin",
        },
        {
            "password": "password123"
        },
    ]
