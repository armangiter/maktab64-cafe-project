from db_models import *
from datetime import datetime


class Orders:

    def __init__(self, id, table_id, number, status):
        self.id = id
        self.table_id = table_id
        self.number = number
        self.status = status
        self.time_stamp = datetime.now()
