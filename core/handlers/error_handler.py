from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum
from core.exceptions.jwt_exception import JWTException


def custom_error_handler(exception: Exception, context: dict) -> Response:
    handlers = {
        'JWTException': _jwt_validate_error
    }
    response = exception_handler(exception, context)
    exception_class = exception.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exception, context)

    return response


def _jwt_validate_error(exception: JWTException, context: dict) -> Response:
    return Response(ErrorEnum.JWT.message, ErrorEnum.JWT.code)
