from core.db_models import *


class OrderItem:
    def __init__(self, order_id, item_id):
        self.order_id = order_id
        self.item_id = item_id
        new_row = Order_items(item_id=self.item_id, order_id=self.order_id)
        session.add(new_row)
        session.commit()

    @classmethod
    def all_order_items(cls):
        order_item = session.query(Order_items).all()
        order_item_dict = {}
        for i in order_item:
            i: Order_items
            order_item_dict[i.id] = {
                'order_id': i.order_id,
                'item_id': i.item_id
            }
        return order_item_dict
