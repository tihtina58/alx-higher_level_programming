#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py
that prints all City objects from the database
"""

import sys
from model_city import Base, State, City
from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(City, State).filter(City.state_id == State.id).all()
    for city_obj, state_obj in objs:
        print("{}: ({}) {}".format(state_obj.name, city_obj.id, city_obj.name))
