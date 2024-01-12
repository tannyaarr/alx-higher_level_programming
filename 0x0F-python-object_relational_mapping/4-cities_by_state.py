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
    cursor = conn.cursor()
    query = """SELECT c.id, c.name, s.name
                FROM cities c
                INNER JOIN states s
                ON c.state_id = s.id
                ORDER BY s.id
            """
    res = cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
