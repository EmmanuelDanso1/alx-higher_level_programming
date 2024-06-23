#!/usr/bin/python3
"""
This Script that lists all states from the database hbtn_0e_0_usa.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""
import MySQLdb
import sys
def list_all_state(username, password, database_name):
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password,db=database_name,port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(rows)
    cur.close()
    db.close()
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
