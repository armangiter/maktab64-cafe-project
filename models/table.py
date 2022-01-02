from db_models import *


class TableModels:

    def __init__(self, table_number, cafe_position, capacity):
        self.table_number = table_number
        self.cafe_position = cafe_position
        self.capacity = capacity

    def create(self):
        new_row = Table(table_number=self.table_number, cafe_position=self.cafe_position,
                        capacity=self.capacity)
        session.add(new_row)
        session.commit()

    @classmethod
    def delete(cls, table_id):
        session.query(Table).filter(Table.table_number == table_id).delete()
        session.commit()
