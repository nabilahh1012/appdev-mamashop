class SignUp:
    count_id = 0

    def __init__(self, first_name, last_name, email, password, phone):
        SignUp.count_id += 1
        self.__user_id = SignUp.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__phone = phone

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def get_user_id(self):
        return self.__user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    def get_last_name(self):
        return self.__last_name

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password
    def get_password(self):
        return self.__password

    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone

class LogIn:
    count_id = 0

    def __init__(self, email, password):
        LogIn.count_id += 1
        self.__user_id = LogIn.count_id
        self.__email = email
        self.__password = password

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def get_user_id(self):
        return self.__user_id

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password
    def get_password(self):
        return self.__password

class AdminLogIn:
    count_id = 0

    def __init__(self, email, password):
        AdminLogIn.count_id += 1
        self.__user_id = AdminLogIn.count_id
        self.__email = email
        self.__password = password

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def get_user_id(self):
        return self.__user_id

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password
    def get_password(self):
        return self.__password

class ContactUs:
    count_id = 0

    def __init__(self, first_name, last_name, email, phone, feedback):
        ContactUs.count_id += 1
        self.__user_id = ContactUs.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__feedback = feedback

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def get_user_id(self):
        return self.__user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    def get_last_name(self):
        return self.__last_name

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone

    def set_feedback(self, feedback):
        self.__feedback = feedback
    def get_feedback(self):
        return self.__feedback
