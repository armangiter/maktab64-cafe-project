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

    def change_status(self, stat="ordered"):
        if self.__status:
            self.__status = stat

    def finish(self):
        self.__status = False

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
