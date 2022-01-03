from db_models import *
from datetime import datetime


class Order:

    def __init__(self, table_id, number, time_stamp=datetime.now()):
        self.table_id = table_id
        self.number = number
        self.time_stamp = time_stamp
        self.__status = 'ordered'
        new_row = Orders(table_id=self.table_id, number=self.number,
                         status=self.get_status, time_stamp=self.time_stamp)
        session.add(new_row)
        session.commit()

    @classmethod
    def change_status(cls, stat="ordered", o_id=None):
        session.query(Orders).filter(Orders.id == o_id).update({'status': stat})
        session.commit()

    def get_status(self):
        return self.__status

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
