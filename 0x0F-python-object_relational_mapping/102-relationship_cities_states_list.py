#!/usr/bin/python3
"""
This script lists all `City` objects from the database `hbtn_0e_101_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL

from relationship_state import Base
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

    cities = session.query(City)

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")