import db_models
from db_models import *

class Cashier(Base):
    def __init__(self, first_name, last_name, phone_number, password, email=None, **extra_information):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number[-9:]
        self.email = email
        self.password = password

        cashier = db_models.Cashier(first_name=self.first_name,last_name=self.last_name,phone_number=self.phone_number
                                    ,password=self.password,email=self.email)
        session.add(cashier)
        session.commit()
