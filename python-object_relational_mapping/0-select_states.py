#!/usr/bin/python3
'''Module to lists all states from the database'''


import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    # create cursor
    cursor = db.cursor()

    # query
    cursor.execute('SELECT * FROM states ORDER BY id')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
