from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
        [
            'password must contain one number (0-9)',
            'password must contain one uppercase letter',
            'password must contain one lowercase letter',
            'password must contain one non-alpha numeric',
            'password min 8 max 20 chars'
        ]
    )

    NAME = (
        r'^[a-zA-Z]{3,15}$',
        'only letters min 3 max 15'
    )

    PHONE = (
        r'^0[56789]\d{8}',
        'invalid phone number'
    )

    def __init__(self, pattern, message: str | list[str]):
        self.pattern = pattern
        self.message = message
