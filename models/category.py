from db_models import *


class CategoryModels:

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
