from core.db_models import *
from datetime import datetime
from core.manager import BaseManager


class Order(BaseManager):

    def __init__(self, table_id, number, time_stamp=datetime.now()):
        self.table_id = table_id
        self.number = number
        self.time_stamp = time_stamp
        self.status = 'ordered'
        new_row = Orders(table_id=self.table_id, number=self.number,
                         status=self.status, time_stamp=self.time_stamp)
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
    def all_orders(cls):
        orders = session.query(Orders).all()
        orders_dict = {}
        for i in orders:
            i: Orders
            orders_dict[i.id] = {
                'table_id': i.table_id,
                'number': i.number,
                'time_stamp': i.time_stamp,
                'status': i.status
            }
        return orders_dict
