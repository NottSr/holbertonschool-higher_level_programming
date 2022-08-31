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
    Save in a var called instances
    """
    inst = session.query(State).order_by(State.id).first()

    """
    If the table states is empty, print Nothing followed by a new line
    otherwise, print first instance id and name values
    """
    if inst is None:
        print("Nothing")
    else:
        print(f"{inst.id}: {inst.name}")
