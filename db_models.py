from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgres://lkfrpdyj:hhUJANbdSKxjUZFbO1Ph0E_R4D4wBhT0@castor.db.elephantsql.com/lkfrpdyj')
session = sessionmaker(bind=engine)()


class Cashier(Base):
    __tablename__ = 'cashier'
    id = Column('id', Integer, unique=True, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    phone = Column('phone', String, unique=True)
    email = Column('email', String, unique=True)
    password = Column('password', String)


class Menu_Items(Base):
    __tablename__ = 'menu'
    id = Column('Id', Integer, unique=True, primary_key=True)
    name = Column('Name', String, unique=True)
    price = Column('Price', Integer, unique=False)
    category = Column('Category', String, unique=False)
    discount = Column('discount', Integer, unique=False)
    serv_time = Column('ServTime', Integer, unique=False)
    st_cooking_time = Column('StCookingTime', Integer)

class Table(Base):
    __tablename__ = 'Table'
    id = Column('id', Integer, unique=True, primary_key=True)
    table_number = Column('table number', Integer, unique=True)
    cafe_position = Column('lastname', String)
    capacity = Column('capacity', Integer, unique=True)

Base.metadata.create_all(engine)
