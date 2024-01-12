#!/usr/bin/python3

"""Takes in argument and displays all values in the states table safe
from mysql injection"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    usr = args[1]
    pwd = args[2]
    db = args[3]
    state_name = args[4]
    ht  = "localhost"
    pt = 3306

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, db=db, port=pt)
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
