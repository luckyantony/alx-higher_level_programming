#!/usr/bin/python3

"""
    A script that lists all City objects from the database hbtn_0e_101_usa
    Takes 3 arguments: mysql username, mysql password and database name
    You must use only one query to the database
    You must use the state relationship to access to the State object
    linked to the City object
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    cities = session.query(City).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))