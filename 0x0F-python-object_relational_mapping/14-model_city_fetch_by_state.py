#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
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
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Cicle that goes through query City and State
    to print instance state name based on state id,
    id and name
    """
    inst_q = session.query(City, State).join(State)

    for inst_c, inst_s in inst_q.all():
        print(f"{inst_s.name}: ({inst_c.id}) {inst_c.name}")

    session.commit()
    session.close()
