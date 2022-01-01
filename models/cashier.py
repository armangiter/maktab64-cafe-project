import db_models
from db_models import *

class Cashier(Base):
    def __init__(self, first_name, last_name, phone_number, password, email=None):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number[-9:]
        self.email = email
        self.password = password

        cashier = db_models.Cashier(first_name=self.first_name,last_name=self.last_name,phone_number=self.phone_number
                                    ,password=self.password,email=self.email)
        session.add(cashier)
        session.commit()

    def __repr__(self) -> str:
            return f"""
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Phone Number: 09{self.phone_number}
        Email Address: {self.email if self.email else '-'}
    """
    @classmethod
    def delete(cls,phone):
        cashier = session.query(Cashier).filter(Cashier.id == phone).delete()
        for i in cashier:
            session.delete(i)
            session.commit()

    def all_cashiers(self):
        cashiers = Cashier.query.all()
        for c in cashiers:
            return c.firstname + c.lastname

    @classmethod
    def check_user(cls, phone_number: str, password: str) :
        if session.query(Cashier).fliter(Cashier.phone == phone_number and Cashier.password == password):
            return True
        return False