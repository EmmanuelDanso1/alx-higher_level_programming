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

<<<<<<< HEAD
    my_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = my_cursor.fetchall()

    for row in rows_selected:
=======
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    
    for row in rows:
>>>>>>> e6dc9b241e263646ae6ca9bbcff17eee5b2bfa73
        print(row)
