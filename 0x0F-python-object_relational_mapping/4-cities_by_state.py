#!/usr/bin/python3

"""
    Lists all cities sorted by id
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id")
    for row in cur.fetchall():
        print(row)