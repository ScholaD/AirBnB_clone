#!/usr/bin/python3
"""So This Defines the BaseModel class."""
from models import storage
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """construct"""

    def __init__(self, *args, **kwargs):
        """ Constructor that initializes a new instance of BaseModel """

        dformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, dformat))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """  updates the updated_at
        attribute with the current datetime when called. """

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """  returns a dictionary representation of the object
        with the class name added as __class__. It also converts the
        created_at and updated_at attributes to ISO format strings """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """ Return string reprsentation of the
        object in the desired format. """
        hello = self.__class__.__name__
        return "[{}] ({}) {}".format(hello, self.id, self.__dict__)
