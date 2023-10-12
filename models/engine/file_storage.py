#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ construct """
    __file_path = "file.json"
    __objects = {}

     def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(newname, obj.id)] = obj
