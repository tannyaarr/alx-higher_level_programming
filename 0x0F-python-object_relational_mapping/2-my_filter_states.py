#!/usr/bin/python3

"""displays all values in the states table where name matches"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    usr, pwd, db, state_name = sys.argv[1], sys.argv[2], sys.argv[3],
    sys.argv[4]
    ht, pt = "localhost", 3306

    conn = MySQLdb.connect(host=ht, port=pt, user=usr, passwd=pwd, db=db)

    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id"\
            .format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
