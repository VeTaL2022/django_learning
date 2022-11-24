import json
from rest_framework.views import APIView
from rest_framework.response import Response


class FileReadWrite:
    _file_name = None

    @classmethod
    def load_users(cls):
        try:
            with open(cls._file_name) as file:
                return json.load(file)
        except (Exception,):
            return []

    @classmethod
    def safe_users(cls, data):
        try:
            with open(cls._file_name, 'w') as file:
                json.dump(data, file)
        except Exception as err:
            return str(err)


class MyAPIView(APIView, FileReadWrite):
    _file_name = 'users.json'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.users = self.load_users()


class UserListCreateView(MyAPIView):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def post(self, *args, **kwargs):
        user = self.request.data
        user['id'] = self.users[-1]['id'] + 1 if self.users else 1
        self.users.append(user)
        self.safe_users(self.users)
        return Response(user)


class UserRetrieveUpdateDestroyView(MyAPIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self._get_user_by_pk(pk)

        if user is None:
            return Response('Not Found')

        return Response(user)

    def put(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')
        user = self._get_user_by_pk(pk)

        if new_user.get('id'):
            del new_user['id']

        user |= new_user
        self.safe_users(self.users)
        return Response(new_user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        index = next((i for i, v in enumerate(self.users) if v['id'] == pk), None)

        if index is None:
            return Response('Not Found')

        del self.users[index]
        self.safe_users(self.users)
        return Response('Deleted')

    def _get_user_by_pk(self, pk):
        user = next((user for user in self.users if user['id'] == pk), None)
        return user
