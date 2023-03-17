#!/usr/bin/python3
'''
Module to prints the first State object from the database hbtn_0e_6_usa
'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.bind = engine

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    res = session.query(State).first()
    if res is None:
        print('Nothing')
    else:
        print('{}: {}'.format(res.id, res.name))

    session.close()
