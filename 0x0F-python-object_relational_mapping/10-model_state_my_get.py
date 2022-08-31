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
    Cicle that goes through query State ordered by id
    to print instance id and name if 'a' is found in name
    """
    found_inst, id_found = 0, 0

    for inst in session.query(State).order_by(State.id):
        if inst.name == argv[4]:
            found_inst += 1
            id_found = inst.id

    if found_inst > 0:
        print(id_found)
    else:
        print("Not found")
