from db_models import *
from datetime import datetime


class Order:

    def __init__(self, table_id, number):
        self.table_id = table_id
        self.number = number
        self.__status = 'ordered'
        new_row = Orders(table_id=self.table_id, number=self.number,
                         status=self.get_status, time_stamp=datetime.now())
        session.add(new_row)
        session.commit()

    def change_status(self, stat="ordered"):
        if self.__status:
            self.__status = stat

    def finish(self):
        self.__status = False

