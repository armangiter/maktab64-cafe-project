from db_models import *


class TableModels:

    def __init__(self, id, table_number, cafe_position, capacity):
        self.id = id
        self.table_number = table_number
        self.cafe_position = cafe_position
        self.capacity = capacity

    def create(self):
        new_row = Table(id=self.id, table_number=self.table_number, cafe_position=self.cafe_position,
                        capacity=self.capacity)
        session.add(new_row)
        session.commit()

    @classmethod
    def delete(cls, table_number):
        session.query(Table).filter(Table.table_number == table_number).delete()
        session.commit()
