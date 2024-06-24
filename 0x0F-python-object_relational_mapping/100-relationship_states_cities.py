#!/usr/bin/python3
"""
This script creates the `State` “California” with the
`City` “San Francisco” from the database `hbtn_0e_100_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    url = {
        "drivername": "mysql+mysqldb",
        "host": "localhost",
        "username": username,
        "password": password,
        "database": db_name,
        "port": 3306
    }

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.commit()