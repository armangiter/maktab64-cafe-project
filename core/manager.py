from sqlalchemy import Column, ForeignKey, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from abc import ABC, abstractmethod

Base = declarative_base()
engine = create_engine('postgresql://postgres:123456@localhost/postgres')
session = sessionmaker(bind=engine)()


class BaseManager(ABC):
    @classmethod
    @abstractmethod
    def create(cls, *args):
    """
    to create an object and save into data base
    """


@classmethod
@abstractmethod
def read(cls, row_id):
    """
    to read data from database
    """


@classmethod
@abstractmethod
def update(cls, column_name, row_id, value):
    """
    to update data in database
    """


@classmethod
@abstractmethod
def delete(cls, row_id):
    """
    to delete data from database
    """


@classmethod
@abstractmethod
def read_all(cls):
    """
    to read all data from one table
    """
