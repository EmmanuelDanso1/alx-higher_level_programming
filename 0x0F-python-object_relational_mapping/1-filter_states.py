#!/usr/bin/python3

"""
This script that lists all `states` with a name starting
with `N` from database `hbtn_0e_0_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import MySQLdb
import sys


if __name__ == '__main__':
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=username, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
