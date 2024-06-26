#!/usr/bin/python3
"""
This script lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state_name (str)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,  user=username, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute(
            "SELECT c.name \
                    FROM cities c INNER JOIN states s \
                    ON c.state_id = s.id WHERE s.name = %s \
                    ORDER BY c.id", 
                    (state_name,)
                    )
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
        print("")

