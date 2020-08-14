#!/usr/bin/python3
"""Unittest for db storage"""
from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os


class DBStorageTest(unittest.TestCase):
    """Defines test for DBStorage"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "not pep8 compliant")

if __name__ == "__main__":
    unittest.main()
