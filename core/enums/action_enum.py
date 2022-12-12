from datetime import timedelta
from enum import Enum


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RESET_PASSWORD = ('reset', timedelta(minutes=10))

    def __init__(self, token_type, expired_time):
        self.token_type = token_type
        self.expired_time = expired_time
