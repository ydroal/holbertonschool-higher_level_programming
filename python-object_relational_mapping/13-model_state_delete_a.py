#!/usr/bin/python3
'''
Module to deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
'''


from sqlalchemy import create_engine, text
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

    find_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in find_state:
        session.delete(state)

    session.commit()
    session.close()
