#!/usr/bin/python3
"""
This is an object relational mapping project with
MySQL and Python
A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
def list_all_state(username, password, database_name):
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],database_name=sys.argv[3],port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(rows)
    cur.close()
    db.close()
if __name__ == "__main__":
    list_all_state(username, password, database_name)