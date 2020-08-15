#!/usr/bin/python3
"""
This module defines class State that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
import models
import sqlalchemy import Column, String
import sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """
    Initialize class State with attribute
        name: (str) name of the state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable="False")

    @property
    def cities(self):
