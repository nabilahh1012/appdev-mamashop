class User:
    count_id = 0

    def __init__(self, namec, credit_card, exp_date, ccv, name, remarks):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__namec = namec
        self.__credit_card = credit_card
        self.__exp_date = exp_date
        self.__ccv = ccv
        self.__name = name
        #self.__collectdt = collectdt
        self.__remarks = remarks

    def get_user_id(self):
        return self.__user_id

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

    def set_user_id(self, user_id):
        self.__user_id = user_id

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


