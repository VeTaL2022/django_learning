import json


class Users:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__users_list = []
        self.__read_file()

    def show_all(self):
        return self.__users_list

    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__users_list = json.load(file)
        except (Exception,):
            try:
                with open(self.__file_name, 'w') as file:
                    json.dump(self.__users_list, file)
            except Exception as err:
                print(err)

    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__users_list, file)
        except Exception as err:
            print(err)


users_json = Users('users.json')

for i in users_json.show_all():
    print(i)
