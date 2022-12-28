from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from ..auto_parks.models import AutoParkModel
from ..auto_parks.serializers import AutoParkSerializer
from .models import UserModel as User
from .permissions import IsSuperUser
from .serializers import AvatarSerializer, UserSerializer

UserModel: User = get_user_model()


class UserCreateView(ListCreateAPIView):
    """
    get:
        List of all Users
    post:
        Post User
    """

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class AdminTools(GenericAPIView, ABC):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    @abstractmethod
    def patch(self, *args, **kwargs):
        pass


class SuperUserTools(AdminTools, ABC):
    permission_classes = (IsSuperUser,)


class UserActivateView(AdminTools):
    """
    Activate user by id
    """

    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: UserModel = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserDeactivateView(AdminTools):
    """
    Deactivate user by id
    """

    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: UserModel = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(SuperUserTools):
    """
    User to Admin by id
    """

    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: UserModel = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(SuperUserTools):
    """
    Admin to User by id
    """

    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: UserModel = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AutoParkListCreateView(GenericAPIView):
    """
    get:
        Get list of all Auto_Parks by User
    post:
        Post Auto_Park by User
    """

    def get_object(self) -> User:
        return self.request.user

    def get(self, *args, **kwargs):
        auto_parks = self.get_object().auto_parks
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        auto_park: AutoParkModel = serializer.save()
        auto_park.users.add(user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)


class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile
