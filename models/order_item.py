from core.db_models import *
from core.manager import BaseManager


class OrderItem(BaseManager):
    def __init__(self, order_id, item_id):
        self.order_id = order_id
        self.item_id = item_id
        self.create(self.order_id, self.item_id)

    @classmethod
    def create(cls, order_id, item_id):
        new_row = Order_items(item_id=item_id, order_id=order_id)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Order_items).filter(Order_items.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Order_items).filter(Order_items.id == row_id).Update({column_name: value})
        session.commit()

    @classmethod
    def delete(cls, row_id):
        session.query(Order_items).filter(Order_items.id == row_id).delete()
        session.commit()

    @classmethod
    def read_all(cls):
        order_item = session.query(Order_items).all()
        order_item_dict = {}
        for i in order_item:
            i: Order_items
            order_item_dict[i.id] = {
                'order_id': i.order_id,
                'item_id': i.item_id
            }
        return order_item_dict
