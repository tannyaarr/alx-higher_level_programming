#!/usr/bin/python3

"""lists all states with the name starting with N from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    usr, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    ht, pt = "localhost", 3306

    conn = MySQLdb.connect(host=ht, port=pt, user=usr, passwd=pwd, db=db)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY\
            states.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
