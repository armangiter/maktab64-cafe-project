from db_models import *


class MenuItems:
    def __init__(self, name, price, category, discount=0, serv_time=20, st_cooking_time=20):
        self.name = name
        self.price = price
        self.category = category
        self.discount = discount
        self.serv_time = serv_time
        self.st_cooking_time = st_cooking_time
