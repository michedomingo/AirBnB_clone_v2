#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import pep8


class UserTest(unittest.TestCase):
    """Defines tests for class User"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.user = User()
        cls.user.first_name = "Kuppa"
        cls.user.last_name = "So"
        cls.user.email = "kuppa@gmail.com"
        cls.user.password = "password123"

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.user

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_subclass(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save(self):
        """Test save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
