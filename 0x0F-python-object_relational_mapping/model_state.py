#!/usr/bin/pythob3
"""
This script lists all lists all `State`
objects from the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

Base =  declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__=="__main__":
     username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
     url = {
             "drivername": "mysql+mysqldb",
             "host": "localhost"
             "username": username,
             "password":password,
             "db": db_name,
             "port": 3306
             }

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_engine(engine)

