#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) < 4:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    data = cur.fetchall()
    for element in data:
        print(element)
