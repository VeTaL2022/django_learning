from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import UserModel as User

from .serializers import EmailSerializer, PasswordSerializer

UserModel: User = get_user_model()


class ActivateUserView(GenericAPIView):
    """
    Activate user by token
    """
    permission_classes = AllowAny,

    @staticmethod
    def post(*args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    """
    Return activation token by posting email
    """
    serializer_class = EmailSerializer
    permission_classes = AllowAny,

    def post(self, *args, **kwargs):
        email = self.request.data
        email_serializer = self.serializer_class(data=email)
        email_serializer.is_valid(raise_exception=True)
        get_email = email_serializer.data.get('email')
        user = get_object_or_404(UserModel, email=get_email)
        EmailService.recovery_password_using_email(user)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    """
    Change password using activation token
    """
    serializer_class = PasswordSerializer
    permission_classes = AllowAny,

    def post(self, *args, **kwargs):
        token = self.kwargs.get('token')
        data = self.request.data
        password_serializer = self.serializer_class(data=data)
        password_serializer.is_valid(raise_exception=True)
        user = JWTService.validate_token(token, RecoveryToken)
        user.set_password(password_serializer.data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)
