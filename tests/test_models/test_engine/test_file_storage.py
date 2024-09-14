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

        self.assertIn(f"BaseModel.{test_model.id}", saved_data)

    def test_reload_method_reloads_saved_objects(self):
        """Test if the reload method correctly loads objects from file."""
        test_model = BaseModel()
        models.storage.new(test_model)
        models.storage.save()

        models.storage._FileStorage__objects = {}
        models.storage.reload()

        self.assertIn(f"BaseModel.{test_model.id}", models.storage.all())

    def test_reload_method_does_not_do_anything_for_non_existent_file(self):
        """Test if reload does not do anything if the file does not exist."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

        initial_objects = models.storage.all().copy()
        models.storage.reload()
        self.assertEqual(initial_objects, models.storage.all())

if __name__ == "__main__":
    unittest.main()
