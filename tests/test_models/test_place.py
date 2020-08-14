#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8


class PlaceTest(unittest.TestCase):
    """Defines tests for class Place"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.place = Place()
        cls.place.city_id = "hawaii808"
        cls.place.user_id = "modern123"
        cls.place.name = "The Modern Honolulu"
        cls.place.description = "The heart of Waikiki"
        cls.place.number_rooms = 375
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 10000
        cls.place.price_by_night = 300
        cls.place.latitude = 21.306944
        cls.place.longitude = -157.858337
        cls.place.amenity_ids = ["amenity321"]

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.place

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_subclass(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'db')
    def test_save(self):
        """Test save"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
