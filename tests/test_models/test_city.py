#!/usr/bin/python3
"""
Unittest for class City
"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os
import pep8


class CityTest(unittest.TestCase):
    """Defines tests for class City"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.city = City()
        cls.city.name = "SF"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.city

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'db')
    def test_save(self):
        """Test save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
