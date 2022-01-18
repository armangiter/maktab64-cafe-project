from core.db_models import *
from core.manager import BaseManager


class CashierModels(BaseManager):
    def __init__(self, first_name, last_name, phone_number, password, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.create(self.first_name, self.last_name, self.phone_number, self.password, self.email)

    @classmethod
    def create(cls, first_name, last_name, phone_number, password, email):
        cashier = Cashier(firstname=first_name, lastname=last_name, phone=phone_number
                          , password=password, email=email)
        session.add(cashier)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Cashier).filter(Cashier.id == row_id)
        session.commit()
        return data

    @classmethod
    def delete(cls, user_id):
        session.query(Cashier).filter(Cashier.id == user_id).delete()
        session.commit()

    @classmethod
    def read_all(cls):
        cashiers = session.query(Cashier).all()
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
    def update(cls, column_name, row_id, value):
        session.query(Cashier).filter(Cashier.id == row_id).Update({column_name: value})
        session.commit()
