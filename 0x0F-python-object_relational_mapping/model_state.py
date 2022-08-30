#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_0_usa
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class

    Attributes
        __tablename__ (str): The table name
        id (int): The State id
        name (str): The State name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
