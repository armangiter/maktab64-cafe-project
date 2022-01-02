from db_models import *


class OrderItem:
    def __init__(self, order_id, item_id):
        self.order_id = order_id
        self.menu_id = item_id
