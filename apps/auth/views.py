from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import UserModel as User

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, ResetPasswordUsingToken

from .serializers import EmailSerializer, PasswordSerializer

UserModel: User = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = AllowAny,

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class ResetPasswordView(GenericAPIView):
    permission_classes = AllowAny,

    def post(self, *args, **kwargs):
        email = self.request.data
        email_serializer = EmailSerializer(data=email)
        email_serializer.is_valid(raise_exception=True)
        get_email = email_serializer.data.get('email')
        user = get_object_or_404(UserModel, email=get_email)
        EmailService.reset_password(user)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    permission_classes = AllowAny,

    def post(self, *args, **kwargs):
        token = self.kwargs.get('token')
        user = JWTService.validate_token(token, ResetPasswordUsingToken)
        data = self.request.data
        password_serializer = PasswordSerializer(data=data)
        password_serializer.is_valid(raise_exception=True)
        user.set_password(password_serializer.data.get('password'))
        user.save()
        return Response(status=status.HTTP_200_OK)
