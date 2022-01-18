from sqlalchemy import Column, ForeignKey, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:Ja55969655@localhost/postgres')
session = sessionmaker(bind=engine)()


class Cashier(Base):
    __tablename__ = 'Cashier'
    id = Column('id', Integer, unique=True, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    phone = Column('phone', String, unique=True)
    email = Column('email', String, unique=True, nullable=True)
    password = Column('password', String)


class Category(Base):
    __tablename__ = "Category"
    id = Column('id', Integer, unique=True, primary_key=True)
    title = Column('title', String)
    root = Column('root', String, default=None)


class Menu_Items(Base):
    __tablename__ = 'Menu'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('Name', String, unique=True)
    price = Column('Price', Integer, unique=False)
    image = Column('image', String, unique=False)
    description = Column('description', String, unique=False)
    category = Column('Category', Integer, ForeignKey('Category.id', ondelete='CASCADE'))
    discount = Column('discount', Integer, unique=False, default=0)
    serv_time = Column('ServTime', Integer, unique=False, default=10)
    st_cooking_time = Column('StCookingTime', Integer, default=10)


class Table(Base):
    __tablename__ = 'Table'
    id = Column('id', Integer, unique=True, primary_key=True)
    table_number = Column('table number', Integer, unique=True)
    cafe_position = Column('cafe_position', String)
    capacity = Column('capacity', Integer)
    status = Column('status', String)


class Orders(Base):
    __tablename__ = "Orders"
    id = Column('id', Integer, unique=True, primary_key=True)
    table_id = Column('table_id', Integer, ForeignKey('Table.id', ondelete='CASCADE'))
    number = Column('number', Integer)
    status = Column('status', String)
    time_stamp = Column('time_stamp', DateTime)


class Receipts(Base):
    __tablename__ = "Receipts"
    id = Column('id', Integer, unique=True, primary_key=True)
    table_id = Column('table_id', Integer, ForeignKey('Table.id', ondelete='CASCADE'))
    total_price = Column('total_price', Integer, default=0)
    final_price = Column('final_price', Integer, default=0)
    time_stamp = Column('time_stamp', DateTime)
    status = Column('status', String, default="Unpaid")


class Order_items(Base):
    __tablename__ = 'Order_items'
    id = Column('id', Integer, unique=True, primary_key=True)
    item_id = Column('item_id', Integer, ForeignKey('Menu.id', ondelete='CASCADE'))
    order_id = Column('order_items', Integer, ForeignKey('Orders.id', ondelete='CASCADE'))


Base.metadata.create_all(engine)
