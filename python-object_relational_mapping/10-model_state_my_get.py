#!/usr/bin/python3
'''
Module to prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
'''


from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.bind = engine

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    res = session.query(State).filter(text('name=:name')).\
        params(name=state_name).first()

    if res:
        print(res.id)
    else:
        print('Not found')

    session.close()
