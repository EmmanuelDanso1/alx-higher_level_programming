#!/usr/bin/python3
"""
 State module
 contains the state class that inherits from import declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """
    class links to the `states` table
    Attributes:
        id(int): id of state
        name(str): name of state
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

