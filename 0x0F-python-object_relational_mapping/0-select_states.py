#!/usr/bin/python3

"""Scripts that lists all states4 from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    ht = "localhost"
    pt = 3306

    conn = MySQLdb.connect(host=ht, port=pt, user=usr, passwd=pwd, databse=db)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        prin(row)

    cursor.close()
    conn.close()
