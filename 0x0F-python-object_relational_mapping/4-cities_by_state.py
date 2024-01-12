#!/usr/bin/python3
"""Script lists all states from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    ht = "localhost"
    pt = 3306

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, database=db, port=pt)
    curs = conn.cursor()
    query = """SELECT c.id, c.name, s.name
                FROM cities c
                INNER JOIN states s
                ON c.state_id = s.id
                ORDER BY s.id
            """
    res = curs.execute(query)
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    conn.close()
