#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import pep8


class StateTest(unittest.TestCase):
    """Defines tests for class State"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.state

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_subclass(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """Test save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
