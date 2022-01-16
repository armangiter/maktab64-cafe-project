from core.db_models import *
from datetime import datetime
from core.manager import BaseManager


class Order(BaseManager):

    def __init__(self, table_id, number, time_stamp=datetime.now()):
        self.table_id = table_id
        self.number = number
        self.time_stamp = time_stamp
        self.status = 'ordered'
        self.create(self.table_id, self.number, self.status, self.time_stamp)

    @classmethod
    def create(cls, table_id, number, time_stamp, status):
        new_row = Orders(table_id=table_id, number=number,
                         status=status, time_stamp=time_stamp)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Orders).filter(Orders.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Orders).filter(Orders.id == row_id).update({column_name: value})
        session.commit()

    @classmethod
    def delete(cls, row_id):
        session.query(Orders).filter(Orders.id == row_id).delete()
        session.commit()

    @classmethod
    def read_all(cls):
        orders = session.query(Orders).all()
        orders_dict = {}
        for i in orders:
            i: Orders
            orders_dict[i.id] = {
                'order_id': i.id,
                'table_id': i.table_id,
                'number': i.number,
                'time_stamp': i.time_stamp,
                'status': i.status
            }
        return orders_dict
