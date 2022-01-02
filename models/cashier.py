import db_models
from db_models import *


class CashierModels:
    def __init__(self, first_name, last_name, phone_number, password, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def create(self):
        cashier = db_models.Cashier(firstname=self.first_name, lastname=self.last_name, phone=self.phone_number
                                    , password=self.password, email=self.email)
        session.add(cashier)
        session.commit()

    @classmethod
    def delete(cls, user_id):
        session.query(Cashier).filter(Cashier.id == user_id).delete()
        session.commit()

    @classmethod
    def all_cashiers(cls):
        cashiers = Cashier.query.all()
        cashier_dict = {}
        for c in cashiers:
            c: Cashier
            cashier_dict[c.id] = {
                'firstname': c.firstname,
                'lastname': c.lastname,
                'phone': c.phone,
                'email': c.email,
                'password': c.password
            }
        return cashier_dict

    @classmethod
    def check_user(cls, phone_number: str, password: str):
        if session.query(Cashier).fliter(Cashier.phone == phone_number and Cashier.password == password):
            return True
        return False
