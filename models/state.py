#!/usr/bin/python3
"""
This module defines class State that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
import models
from os import getenv


class State(BaseModel):
    """
    Initialize class State with attribute
        name: (str) name of the state
    """
    name = ""
