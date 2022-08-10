#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os
import pycodestyle
from models.engine.file_storage import FileStorage


class test_basemodel(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """ set up class """
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ tear down class at end of testing """
        del cls.base

    def test_docstrings(self):
        """ test for docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """ test initialization """
        self.assertIsInstance(self.base, BaseModel)

    def test_atrributes(self):
        """ test attributes """
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_methods(self):
        """ test methods present """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_todict(self):
        """ test dictionary created """
        n = self.base.to_dict()
        self.assertEqual(dict, type(n))

    def test_save(self):
        """ Testing save """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "skip demo")
    def test_delete(self):
        """ Test delete """
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
