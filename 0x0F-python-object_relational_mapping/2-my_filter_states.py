#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) < 5:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states WHERE states.name\
                           LIKE BINARY '{}' ORDER BY states.id ASC"
                           .format(argv[4]))

    data = cur.fetchall()
    for element in data:
        print(element)

    cur.close()
    db.close()
