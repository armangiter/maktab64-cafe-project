from core.db_models import *
from core.manager import BaseManager


class CategoryModels(BaseManager):

    def __init__(self, title, root=None):
        self.title = title
        self.root = root
        self.create(self.title, self.root)

    @classmethod
    def create(cls, title, root):
        new_row = Category(title=title, root=root)
        session.add(new_row)
        session.commit()

    @classmethod
    def read(cls, row_id):
        data = session.query(Category).filter(Category.id == row_id)
        return data

    @classmethod
    def update(cls, column_name, row_id, value):
        session.query(Category).filter(Category.id == row_id).Update({column_name: value})
        session.commit()

    @classmethod
    def delete(cls, category_id):
        session.query(Category).filter(Category.id == category_id).delete()
        session.commit()

    @classmethod
    def read_all(cls):
        categories = session.query(Category).all()
        categories_dict = {}
        for i in categories:
            i: Category
            categories_dict[i.id] = {
                'id': i.id,
                'title': i.title,
                'root': i.root
            }
        return categories_dict
