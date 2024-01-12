#!/usr/bin/python3

"""Scripts that lists all states4 from the database hbtn_0e_0_usa"""

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
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
