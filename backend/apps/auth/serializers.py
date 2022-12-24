from django.contrib.auth import get_user_model

from rest_framework.serializers import EmailField, ModelSerializer, Serializer

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class EmailSerializer(Serializer):
    email = EmailField()


class PasswordSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = 'password',
