#!/usr/bin/python3

"""lists all cities from the data base hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    ht  = "localhost"
    pt = 3306

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, db=db, port=pt)
    cursor = conn.cursor()
     query = """SELECT c.id, c.name, s.name
                FROM cities c
                INNER JOIN states s
                ON c.state_id = s.id
                ORDER BY s.id
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
