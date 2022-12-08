import os
from uuid import uuid1


def upload_photo(instance, file: str) -> str:
    extension = file.split('.')[-1]
    return os.path.join('cars', f'{instance.car.id}', f'{uuid1()}.{extension}')
