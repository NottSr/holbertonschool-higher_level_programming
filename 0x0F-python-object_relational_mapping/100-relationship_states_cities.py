#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Creating connection to mysql using arguments
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        )
    )
    """
    Setting up and starting session
    """
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Creating the new instances
    """
    new_state = State(name='California')
    new_city = City(name='San Francisco')

    """
    Append the instance new_city to new_state
    and updating the new info by adding new_state
    """
    new_state.cities.append(new_city)
    session.add(new_state)

    session.commit()
    session.close()
