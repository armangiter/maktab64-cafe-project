from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, foreign

Base = declarative_base()
engine = create_engine('postgres://lkfrpdyj:hhUJANbdSKxjUZFbO1Ph0E_R4D4wBhT0@castor.db.elephantsql.com/lkfrpdyj')
session = sessionmaker(bind=engine)()


class Cashier(Base):
    __tablename__ = 'Cashier'
    id = Column('id', Integer, unique=True, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    phone = Column('phone', String, unique=True)
    email = Column('email', String, unique=True)
    password = Column('password', String)


class Menu_Items(Base):
    __tablename__ = 'Menu'
    id = Column('Id', Integer, unique=True, primary_key=True)
    name = Column('Name', String, unique=True)
    price = Column('Price', Integer, unique=False)
    category = Column('Category', String, unique=False, foreign_key='category.id')
    discount = Column('discount', Integer, unique=False, default=0)
    serv_time = Column('ServTime', Integer, unique=False, default=10)
    st_cooking_time = Column('StCookingTime', Integer, default=10)


class Table(Base):
    __tablename__ = 'Table'
    id = Column('id', Integer, unique=True, primary_key=True)
    table_number = Column('table number', Integer, unique=True)
    cafe_position = Column('lastname', String)
    capacity = Column('capacity', Integer, unique=True, default=2)


class Category(Base):
    __tablename__ = "Category"
    id = Column('id', Integer, unique=True, primary_key=True)
    title = Column('title', String)
    root = Column('root', String, default=None)



Base.metadata.create_all(engine)
