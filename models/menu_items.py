from core.db_models import *
from core.manager import BaseManager


class MenuItems(BaseManager):
    def __init__(self, name, price, image, description, category, discount=0, serv_time=20, st_cooking_time=20):
        self.name = name
        self.price = price
        self.image = image
        self.description = description
        self.category = category
        self.discount = discount
        self.serv_time = serv_time
        self.st_cooking_time = st_cooking_time
        self.create(self.name, self.price, self.image, self.description, self.category, self.discount, self.serv_time,
                    self.st_cooking_time)

    @classmethod
    def create(cls, name, price, image, description, category, discount, serv_time, st_cooking_time):
        new_row = Menu_Items(name=name, price=price, image=image, description=description,
                             category=category,
                             discount=discount, serv_time=serv_time, st_cooking_time=st_cooking_time)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Menu_Items).filter(Menu_Items.id == row_id).one()
        item = {
            'id': data.id,
            'name': data.name,
            'price': data.price,
            'image': data.image,
        }
        return item

    @classmethod
    def delete(cls, item_id):
        session.query(Menu_Items).filter(Menu_Items.id == item_id).delete()
        session.commit()

    @classmethod
    def read_all(cls):
        menu = session.query(Menu_Items).all()
        menu_dict = {}
        for i in menu:
            i: Menu_Items
            menu_dict[i.id] = {
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'image': i.image,
                'description': i.description,
                'category': i.category,
                'discount': i.discount,
                'serv_time': i.serv_time,
                'st_cook_time': i.st_cooking_time
            }
        return menu_dict

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Menu_Items).filter(Menu_Items.id == row_id).update({column_name: value})
        session.commit()
