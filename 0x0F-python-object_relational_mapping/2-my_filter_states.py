#!/usr/bin/python3
"""
This script lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_searched_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format( state_searched_name)
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)

