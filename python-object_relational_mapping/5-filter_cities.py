#!/usr/bin/python3
'''
Module to takes in the name of a state as an argument
and lists all cities of that state, using the database.
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

    sql = "SELECT cities.name FROM states\
           LEFT JOIN cities ON states.id = cities.state_id\
           WHERE states.name LIKE BINARY %s\
           ORDER BY cities.id"
 
    cursor.execute(sql, (state_name, ))

    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    list_cities = ', '.join(cities)
    print(list_cities)
    cursor.close()
    db.close()
