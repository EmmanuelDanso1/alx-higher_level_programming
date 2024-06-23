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
    state_name_searched = sys.argv[4]
    db = MySQLdb.connect(user=username, passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id", ( state_name_searched)
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
