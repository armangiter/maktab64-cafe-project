from core.db_models import *
from datetime import datetime
from core.manager import BaseManager


class Receipt(BaseManager):

    def __init__(self, table_id, total_price, final_price, status='Unpaid', time_stamp=datetime.now()):
        self.table_id = table_id
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = time_stamp
        self.status = status
        self.create(self.table_id, self.total_price, self.final_price, self.status, self.time_stamp)

    @classmethod
    def create(cls, table_id, total_price, final_price, status, time_stamp):
        new_row = Receipts(table_id=table_id, total_price=total_price, final_price=final_price,
                           status=status, time_stamp=time_stamp)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Receipts).filter(Receipts.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Receipts).filter(Receipts.table_id == row_id).update({column_name: value})
        session.commit()

    @classmethod
    def read_all(cls):
        receipts = session.query(Receipts).all()
        receipts_dict = {}
        for i in receipts:
            receipts_dict[i.id] = {
                'id': i.id,
                'table_id': i.table_id,
                'total_price': i.total_price,
                'final_price': i.final_price,
                'time_stamp': i.time_stamp,
                'status': i.status,
            }
        return receipts_dict

    @classmethod
    def delete(cls, row_id):
        session.query(Receipts).filter(Receipts.table_id == row_id).delete()
        session.commit()
