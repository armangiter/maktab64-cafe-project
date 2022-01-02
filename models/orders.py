from db_models import *
from datetime import datetime


class Orders:

    def __init__(self, table_id, number):
        self.table_id = table_id
        self.number = number
        self.__status = 'ordered'
        self.time_stamp = datetime.now()

    def change_status(self, stat="ordered"):
        if self.__status:
            self.__status = stat

    def finish(self):
        self.__status = False
