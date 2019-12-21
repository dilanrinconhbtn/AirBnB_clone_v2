#!/usr/bin/python3
"""This is the state class"""
import models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """getter attribute to return list of city instance"""
        city_list = []
        for value in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(value)
        return(city_list)
