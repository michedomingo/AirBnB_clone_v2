#!/usr/bin/python3
"""
Unittest for class BaseModel
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import pep8


class BaseModelTest(unittest.TestCase):
    """Defines tests for class BaseModel"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        cls.base = BaseModel()

    @classmethod
    def teardown(cls):
        """Teardown test"""
        del cls.base

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method(self):
        """Test Basemodel methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'db')
    def test_save(self):
        """Test save"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """Test convert to dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
