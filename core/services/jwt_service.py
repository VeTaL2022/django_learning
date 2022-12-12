from typing import Type

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from apps.users.models import UserModel as User

from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JWTException

UserModel: User = get_user_model()
TokenClass = Type[BlacklistMixin | Token]


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.expired_time
    token_type = ActionEnum.ACTIVATE.token_type


class ResetPasswordUsingToken(BlacklistMixin, Token):
    lifetime = ActionEnum.RESET_PASSWORD.expired_time
    token_type = ActionEnum.RESET_PASSWORD.token_type


class JWTService:
    @staticmethod
    def create_token(user, token_class: TokenClass):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: TokenClass):
        try:
            token_resolve = token_class(token)
            token_resolve.check_blacklist()
        except (Exception,):
            print('Error')
            raise Exception
            # raise JWTException
        token_resolve.blacklist()
        user_id = token_resolve.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
