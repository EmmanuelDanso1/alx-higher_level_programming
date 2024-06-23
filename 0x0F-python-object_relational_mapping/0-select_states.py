#!/usr/bin/python3

import MySQLdb
import sys

def list_all_states(username, password, dbname):

    
    if __name__ == "__main__":
        
        # connecting to MySQLdb database
        db = MySQLdb.connect(host="localhost", user="sys.argv[1]", passwd="sys.argv[2]",db="sys.argv[3]",port=3306)
    
        # creating cursor object to interact with database
        cur = db.cursor()
    
        # executing query to list all states
        cur.execute("SELECT * FROM states ORDER_BY id ASC")
    
        # fetching all from execute query
        rows = cur.fetchall()
    
        # looping through rows and printing eachone
        for row in rows:
            print(row)
    
        # cleaning up the cursor and database
        cur.close()
        db.close()
    