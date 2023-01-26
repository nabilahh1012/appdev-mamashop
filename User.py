class LogIn:
    count_id = 0

    def __init__(self, username, password):
        LogIn.count_id += 1
        self.__user_id = LogIn.count_id
        self.__username = username
        self.__password = password

    def get_user_id(self):
        return self.__user_id
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

class SignUp:
    count_id = 0

    def __init__(self, username, password, phone):

        SignUp.count_id += 1
        self.__user_id = SignUp.count_id
        self.__username = username
        self.__password = password
        self.__phone = phone

    def get_user_id(self):
        return self.__user_id
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

    def get_phone(self):
        return self.__phone
    def set_phone(self, phone):
        self.__phone = phone
