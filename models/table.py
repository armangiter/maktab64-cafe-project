from db_models import *


class Table:

    def __init__(self, table_number, cafe_position, capacity):
        self.table_number = table_number
        self.cafe_position = cafe_position
        self.capacity = capacity
