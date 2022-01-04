from models.DB_MODELS.db_models import *


class MenuItems:
    def __init__(self, name, price, image, description, category, discount=0, serv_time=20, st_cooking_time=20):
        self.name = name
        self.price = price
        self.image = image
        self.description = description
        self.category = category
        self.discount = discount
        self.serv_time = serv_time
        self.st_cooking_time = st_cooking_time
        new_row = Menu_Items(name=self.name, price=self.price, image=self, description=self.description,
                             category=self.category,
                             discount=self.discount, serv_time=self.serv_time, st_cooking_time=self.st_cooking_time)
        session.add(new_row)
        session.commit()

    @classmethod
    def delete_item(cls, item_id):
        session.query(Menu_Items).filter(Menu_Items.id == item_id).delete()
        session.commit()

    @classmethod
    def all_menu_item(cls):
        menu = session.query(Menu_Items).all()
        menu_dict = {}
        for i in menu:
            i: Menu_Items
            menu_dict[i.id] = {
                'name': i.name,
                'price': i.price,
                'category': i.category,
                'discount': i.discount,
                'serv_time': i.serv_time,
                'st_cook_time': i.st_cooking_time
            }
        return menu_dict

    @classmethod
    def update(cls, attr, i_id, value):
        session.query(Menu_Items).filter(Menu_Items.id == i_id).update({attr: value})
        session.commit()
