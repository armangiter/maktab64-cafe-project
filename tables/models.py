from core.db_config import Base
from sqlalchemy import Column, String, Integer


class Table(Base):
    __tablename__ = 'Table'
    id = Column('id', Integer, unique=True, primary_key=True)
    table_number = Column('table number', Integer, unique=True)
    cafe_position = Column('lastname', String)
    capacity = Column('capacity', Integer, unique=True)
