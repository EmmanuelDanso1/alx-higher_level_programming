#!/usr/bin/python3
"""
This script lists all lists all `State`
objects from the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    url = {
        "drivername": "mysql+mysqldb",
        "host": "localhost",
        "username": username,
        "password": password,
        "db": db_name,
        "port": 3306
    } 
    

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    q = session.query(State).order_by(State.id)

    for instance in q:
        print("{}: {}".format(instance.id, instance.name))
