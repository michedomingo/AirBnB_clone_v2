#!/usr/bin/python3
"""
This module defines class Review that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Review(BaseModel, Base):
    """
    Initialize class Review with attributes
        place_id: (str) place id
        user_id: (str) user id
        text: (str)
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
