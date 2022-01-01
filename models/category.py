
from db_models import *

class Calegory_models:

    def __init__(self,title,root=None):
        self.title=title
        self.root=root

    def craete_category(self):
        new_row= Category(title=self.title, root=self.root)

        session.add(new_row)
        session.commit()

    @classmethod
    def delete(cls, title):
        session.query(Calegory_models).filter(Calegory_models.title == title).delete()
        session.commit()

