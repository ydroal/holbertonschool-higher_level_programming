#!/usr/bin/python3
'''Module to lists all states from the database'''


import MySQLdb


# connect to database
db = MySQLdb.connect(host='localhost', port=3306, user='root',
                     passwd='root', db='hbtn_0e_0_usa')

# create cursor
cursor = db.cursor()

# query
cursor.execute('SELECT * FROM states ORDER BY id')

rows = cursor.fetchall()
for row in rows:
    print(row)
