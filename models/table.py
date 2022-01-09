from core.db_models import *
from core.manager import BaseManager


class TableModels(BaseManager):

    def __init__(self, table_number, cafe_position, capacity):
        self.table_number = table_number
        self.cafe_position = cafe_position
        self.capacity = capacity
        new_row = Table(table_number=self.table_number, cafe_position=self.cafe_position,
                        capacity=self.capacity)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Table).filter(Table.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Table).filter(Table.id == row_id).Update({column_name: value})

    @classmethod
    def delete(cls, table_id):
        session.query(Table).filter(Table.table_number == table_id).delete()
        session.commit()

    @classmethod
    def all_table(cls):
        tables = session.query(Table).all()
        table_dict = {}
        for i in tables:
            i: Table
            table_dict[i.id] = {
                'table_number': i.table_number,
                'cafe_position': i.cafe_position,
                'capacity': i.capacity
            }
        return table_dict
