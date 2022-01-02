from db_models import *


class OrderItem:
    def __init__(self, order_id, item_id):
        self.order_id = order_id
        self.item_id = item_id
        new_row = Order_items(item_id=self.item_id, order_id=self.order_id)
        session.add(new_row)
        session.commit()
