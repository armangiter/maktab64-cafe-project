from db_models import *
from datetime import datetime


class Orders:

    def __init__(self, id, table_id, number):
        self.id = id
        self.table_id = table_id
        self.number = number
        self.__status = 'ordered'
        self.time_stamp = datetime.now()

    def change_status(self, stat="ordered"):
        self.__status = stat
