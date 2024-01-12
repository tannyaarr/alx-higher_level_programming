#!/usr/bin/python3
"""Script lists all cities of a specific state from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    usr, pwd, db, state_name = sys.argv[1:5]
    ht, pt = "localhost", 3306

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, database=db, port=pt)
    cursor = conn.cursor()

    query = """SELECT c.id, c.name, s.name
                FROM cities c
                INNER JOIN states s
                ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id
            """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

