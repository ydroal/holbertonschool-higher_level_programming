#!/usr/bin/python3
'''
Module to takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
'''


import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    sql = "SELECT * FROM states\
           WHERE name LIKE BINARY %s\
           ORDER BY id"

    cursor.execute(sql, (state_name, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
