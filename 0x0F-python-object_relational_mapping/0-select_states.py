#!/usr/bin/python3

"""
Scripts that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    ht = "localhost"
    pt = 3306

    db = MySQLdb.connect(hostt=ht, port=pt, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        prin(row)

    cursor.close()
    db.close()
