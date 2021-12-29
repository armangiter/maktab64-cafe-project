from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgres://lkfrpdyj:hhUJANbdSKxjUZFbO1Ph0E_R4D4wBhT0@castor.db.elephantsql.com/lkfrpdyj')
session = sessionmaker(bind=engine)()


class Menu_Items(Base):
    __tablename__ = 'menu'
    id = Column('Id', Integer, unique=True, primary_key=True)
    name = Column('Name', String, unique=True)
    price = Column('Price', Integer, unique=False)
    category = Column('Category', String, unique=False)
    discount = Column('discount', Integer, unique=False)
    serv_time = Column('ServTime', Integer, unique=False)
    st_cooking_time = Column('StCookingTime', Integer)


Base.metadata.create_all(engine)
