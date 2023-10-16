#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
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
		for key in FileStorage.__objects:
			object_details = FileStorage.__objects[key].to_dict()
			transformed[key] = object_details
		with open(FileStorage.__file_path, mode="w") as f:
			json.dump(transformed, f)

	def reload(self):
		"""
		Deserializes data from a JSON file into __objects if the file exists.
		"""
		from models.user import User
		from models.city import City
		from models.place import Place
		from models.state import State
		from models.review import Review
		from models.amenity import Amenity
		from models.base_model import BaseModel

		cls_mapp = {
				"Place": Place,
				"State": State,
				"Review": Review,
				"Amenity": Amenity,
				"BaseModel": BaseModel,
				"User": User, "City": City
		}

		try:
			with open(FileStorage.__file_path, mode="r") as f:
				dict_readed = json.load(f)
				for values in dict_readed.values():
					class_name = values['__class__']
					real_class = cls_mapp[class_name]
					self.new(real_class(**values))
		except FileNotFoundError:
			return
