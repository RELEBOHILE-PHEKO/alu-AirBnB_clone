#!/usr/bin/python3
"""Module file_storage.

This Module contains a definition for FileStorage Class.
"""
import importlib
import json
import os
import re


class FileStorage:
    """FileStorage Class.

    This class manages storage of hbnb models in JSON format.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        json_objects = {
            key: val.to_dict() for key, val in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = self.get_class(
                    key.split('.')[0])(**jo[key])
        except FileNotFoundError:
            pass

    def get_class(self, name):
        """Return a class from models module using its name.

        Args:
            name (str): The name of the class.

        Returns:
            type: The class.
        """
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
