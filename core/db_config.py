from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgres://lkfrpdyj:hhUJANbdSKxjUZFbO1Ph0E_R4D4wBhT0@castor.db.elephantsql.com/lkfrpdyj')
session = sessionmaker(bind=engine)()
