#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up test cases."""
        self.test_file = "test_file.json"
        models.storage._FileStorage__file_path = self.test_file
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after test cases."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_save_method_saves_objects_to_file(self):
        """Test if the save method saves objects to file."""
        test_model = BaseModel()
        models.storage.new(test_model)
        models.storage.save()

        with open(self.test_file, "r") as f:
            saved_data = json.load(f)

        key = f"BaseModel.{test_model.id}"
        self.assertIn(key, saved_data)
        self.assertEqual(saved_data[key]["id"], test_model.id)
        self.assertEqual(saved_data[key]["__class__"], "BaseModel")

    def test_reload_method_reloads_saved_objects(self):
        """Test if the reload method correctly loads objects from file."""
        test_model = BaseModel()
        models.storage.new(test_model)
        models.storage.save()

        models.storage._FileStorage__objects = {}
        models.storage.reload()

        key = f"BaseModel.{test_model.id}"
        self.assertIn(key, models.storage.all())
        reloaded_obj = models.storage.all()[key]
        self.assertEqual(reloaded_obj.id, test_model.id)
        self.assertIsInstance(reloaded_obj, BaseModel)

    def test_reload_method_does_not_do_anything_for_non_existent_file(self):
        """Test if reload does not do anything if the file does not exist."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

        initial_objects = models.storage.all().copy()
        models.storage.reload()
        self.assertEqual(initial_objects, models.storage.all())

    def test_all_method_returns_dict(self):
        """Test if all method returns a dictionary."""
        self.assertIsInstance(models.storage.all(), dict)

    def test_new_method_adds_object(self):
        """Test if new method adds an object to storage."""
        test_model = BaseModel()
        models.storage.new(test_model)
        key = f"BaseModel.{test_model.id}"
        self.assertIn(key, models.storage.all())

if __name__ == "__main__":
    unittest.main()
