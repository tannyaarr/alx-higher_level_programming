#!/usr/bin/python3

"""
Scripts that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows = cursor.fetchall()

    for row in rows:
        prin(row)

    cursor.close()
    db.close()
