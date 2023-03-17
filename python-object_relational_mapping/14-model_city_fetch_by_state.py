#!/usr/bin/python3
'''
Module to prints all City objects from the database hbtn_0e_14_usa
'''


from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    res = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for state, city in res:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
