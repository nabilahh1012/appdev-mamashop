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

class Payment:
    count_id = 0

    def __init__(self, namec, credit_card, exp_date, ccv, name, remarks):
        Payment.count_id += 1
        self.__payment_id = Payment.count_id
        self.__namec = namec
        self.__credit_card = credit_card
        self.__exp_date = exp_date
        self.__ccv = ccv
        self.__name = name
        #self.__collectdt = collectdt
        self.__remarks = remarks

    def get_payment_id(self):
        return self.__payment_id

    def get_namec(self):
        return self.__namec

    def get_credit_card(self):
        return self.__credit_card

    def get_exp_date(self):
        return self.__exp_date

    def get_name(self):
        return self.__name

    def get_ccv(self):
        return self.__ccv

    #def get_collectdt(self):
      #  return self.__collectdt

    def get_remarks(self):
        return self.__remarks

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def set_namec(self, namec):
        self.__namec = namec

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card

    def set_exp_date(self, exp_date):
        self.__exp_date = exp_date

    def set_ccv(self, ccv):
        self.__ccv = ccv

    def set_name(self, name):
       self.__name = name

    #def set_collectdt(self,collectdt):
       # self.__collectdt = collectdt

    def set_remarks(self, remarks):
        self.__remarks = remarks

class PickUp:
    count_id = 0
    def __init__(self, username, phone,location,timing):
        PickUp.count_id += 1
        self.__pickup_id = PickUp.count_id
        self.__username = username
        self.__phone = phone
        self.__location = location
        self.__timing = timing

    def get_pickup_id(self):
        return self.__pickup_id
    def set_pickup_id(self, pickup_id):
        self.__pickup_id = pickup_id

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_phone(self):
        return self.__phone
    def set_phone(self, phone):
        self.__phone = phone

    def get_location(self):
        return self.__location
    def set_location(self, location):
        self.__location = location

    def get_timing(self):
        return self.__timing
    def set_timing(self, timing):
        self.__timing= timing

class Product:
    count_id = 0

    def __init__(self, name, quantity, price, total):
        Product.count_id += 1
        self.__product_id = Product.count_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__total = total
    #
    # def __init__(self, name, quantity, price, total):
    #     Product.count_id += 1
    #     self.__product_id = Product.count_id
    #     self.__name = name
    #     self.__quantity = quantity
    #     self.__price = price
    #     self.__total = total

    def get_product_id(self):
        return self.__product_id
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_total(self):
        return self.__total
    def set_total(self, total):
        self.__total = total
