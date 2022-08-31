#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
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
    Session = sessionmaker(engine)
    session = Session()

    """
    Save in a dict
    """
    instances = session.query(State).order_by(State.id)

    if instances is not None:
        print(f"{instances[0].id}: {instances[0].name}")
    else:
        print("Nothing")
