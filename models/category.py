from core.db_models import *
from core.manager import BaseManager

class CategoryModels(BaseManager):

    def __init__(self, title, root=None):
        self.title = title
        self.root = root
        new_row = Category(title=self.title, root=self.root)
        session.add(new_row)
        session.commit()

    @classmethod
    def delete(cls, category_id):
        session.query(Category).filter(Category.id == category_id).delete()
        session.commit()

    @classmethod
    def all_categories(cls):
        categories = session.query(Category).all()
        categories_dict = {}
        for i in categories:
            i: Category
            categories_dict[i.id] = {
                'title': i.title,
                'root': i.root
            }
        return categories_dict
