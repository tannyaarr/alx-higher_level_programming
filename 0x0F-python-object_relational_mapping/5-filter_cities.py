#!/usr/bin/python3
"""Script lists all cities of a specific state from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    state_name = args[4]
    ht = "localhost"
    pt = 3306

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, database=db, port=pt)
    cursor = conn.cursor()

    query = """SELECT name
                FROM cities 
                WHERE state_id = (
                SELECT id
                FROM states
                WHERE name = '{}'
                )
                ORDER BY id
            """.format(state_name)
    res = cursor.execute(query)
    rows = cursor.fetchall()
    city_names = ', '.join(row[0] for row in rows)
    print(city_names)

    cursor.close()
    conn.close()
