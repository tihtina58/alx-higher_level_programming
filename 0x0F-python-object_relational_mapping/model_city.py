#!/usr/bin/python3
"""
Python file that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """City class."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    states = relationship("State")
