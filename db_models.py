from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:mahdi12345M@localhost/flash_cards')
session = sessionmaker(bind=engine)()
