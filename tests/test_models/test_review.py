#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
import pep8


class ReviewTest(unittest.TestCase):
    """Defines tests for class Review"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.rev = Review()
        cls.rev.place_id = "modern_honolulu321"
        cls.rev.user_id = "modern123"
        cls.rev.text = "Cool hotel"

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.rev

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_subclass(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'db')
    def test_save(self):
        """Test save"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
