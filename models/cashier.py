import db_models
from db_models import *
from json import dumps



class CashierError(Exception):
    def __init__(self, msg: str, field: str, data: ...) -> None:
        super().__init__(msg, field, data)
        self.msg = msg
        self.field = field
        self.data = data
    def __str__(self):
        return f"error on field `{self.field}` (invalid data: `{self.data}`): {self.msg}"

class Cashier(Base):
    def __init__(self, first_name, last_name, phone_number, password, email=None, **extra_information):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number[-9:]
        self.email = email
        self.password = password
        self.extra_information = dumps(extra_information)

        cashier = db_models.Cashier(first_name=self.first_name,last_name=self.last_name,phone_number=self.phone_number
                                    ,password=self.password,email=self.email)