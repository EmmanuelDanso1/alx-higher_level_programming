#!/usr/bin/python3
"""
This script adds the `State` object “Louisiana”
to the database `hbtn_0e_6_usa`.

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
    username, passw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    url = {
        "drivername": "mysql+mysqldb",
        "host": "localhost",
        "username": username,
        "password": passw,
        "database": db_name,
        "port":3306
    }

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print(new.id)