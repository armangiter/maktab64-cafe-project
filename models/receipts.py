from table import *
from db_models import *
from datetime import datetime


class Receipts_model:

    def __init__(self, table_id, total_price=0, final_price=0):
        self.table_id = table_id
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = datetime.now()

    def create(self):
        new_row = Receipts(table_id=self.table_id, total_price=self.total_price, final_price=self.final_price,
                           time_stamp=self.time_stamp)
        session.add(new_row)
        session.commit()

    def show_all(self):
        receipts = session.query(Receipts).all()
        for i in receipts:
            return i

    @classmethod
    def delete(cls, table_id):
        session.query(Receipts).filter(Receipts.table_id == table_id).delete()
        session.commit()

    @classmethod
    def update(cls):
        pass



