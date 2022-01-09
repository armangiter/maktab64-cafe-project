from core.db_models import *
from datetime import datetime
from core.manager import BaseManager


class Receipt(BaseManager):

    def __init__(self, table_id, total_price=None, final_price=0, time_stamp=datetime.now()):
        self.table_id = table_id
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = time_stamp
        new_row = Receipts(table_id=self.table_id, total_price=self.total_price, final_price=self.final_price,
                           time_stamp=self.time_stamp)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Receipts).filter(Receipts.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Receipts).filter(Receipts.id == row_id).Update({column_name : value})
        session.commit()

    @classmethod
    def all_receipts(cls):
        receipts = session.query(Receipts).all()
        receipts_dict = {}
        for i in receipts:
            receipts_dict[i.id] = {
                'table_id': i.table_id,
                'total_price': i.total_price,
                'final_price': i.final_price,
                'time_stamp': i.time_stamp
            }
        return receipts_dict

    @classmethod
    def delete(cls, receipt_id):
        session.query(Receipts).filter(Receipts.table_id == receipt_id).delete()
        session.commit()
