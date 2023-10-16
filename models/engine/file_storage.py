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
<<<<<<< HEAD

=======
>>>>>>> f09c4c0cbbdced4b99872896e6d6b30adae666c8
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(newname, obj.id)] = obj

    def save(self):
        """ serializes objectss to the JSON file """
        transformed = {}
<<<<<<< HEAD
        for key in FileStorage.__objects:
            object_details = FileStorage.__objects[key].to_dict()
            transformed[key] = object_details
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(transformed, f)

    def reload(self):
        """Deserializes data from a
        JSON file into __objects if the file exists."""
=======
        for key in self.__objects:
            object_details = self.__objects[key].to_dict()
            transformed[key] = object_details
        with open(self.__file_path, mode="w") as f:
            json.dump(transformed, f)

    def reload(self):
        """
        Deserializes data from a JSON file into __objects if the file exists.
        """
>>>>>>> f09c4c0cbbdced4b99872896e6d6b30adae666c8

        try:
            with open(FileStorage.__file_path, mode="r") as f:
                readed = json.load(f)
            for key, dict_readed in readed.items():
                class_name = dict_readed['__class__']
                new_object = eval(class_name)(**dict_readed)
                self.new(new_object)
        except FileNotFoundError:
            return
