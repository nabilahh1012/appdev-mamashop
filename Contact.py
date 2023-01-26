class ContactUs:
    count_id = 0

    def __init__(self, first_name, last_name, email, phone, remarks):
        ContactUs.count_id += 1
        self.__contactus_id = ContactUs.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__remarks = remarks

    def get_contactus_id(self):
        return self.__contactus_id
    def set_contactus_id(self, contactus_id):
        self.__contactus_id = contactus_id

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone
    def set_phone(self, phone):
        self.__phone = phone

    def get_remarks(self):
        return self.__remarks
    def set_remarks(self, remarks):
        self.__remarks = remarks
