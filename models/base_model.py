#!/usr/bin/python3
"""
This module defines class BaseModel  for all models in our hbnb clone
"""

import uuid
from datetime import datetime
import models
from sqlalchemy import Integer, String , Column, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel class / Instantiates a new model"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        try:
            self.id
        except Exception:
            self.id = str(uuid.uuid4())
        try:
            self.created_at
        except Exception:
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        base_dict = {}
        base_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in base_dict:
            del base_dict["_sa_instance_state"]
        if self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, datetime):
                    value = value.isoformat()
                base_dict[key] = value
        return base_dict

    def delete(self):
        """delete the current instance from the storage (models.storage) """
        models.storage.delete(self)
