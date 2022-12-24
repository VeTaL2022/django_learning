import os
from uuid import uuid1


def upload_avatar(instance, file: str) -> str:
    extension = file.split('.')[-1]
    return os.path.join(instance.user.email, 'avatars', f'{uuid1()}.{extension}')
