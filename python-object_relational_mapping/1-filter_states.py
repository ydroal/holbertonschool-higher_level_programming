#!/usr/bin/python3
'''Module to lists all states with a name starting with N from the database'''


import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    sql = "SELECT * FROM states\
           WHERE name LIKE BINARY 'N%'\
           ORDER BY id"

    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
