#!/usr/bin/python3
"""Unittest for Base class which has Rectangle, square
class
"""


import unittest
import json
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):
    """Defining the test class Base"""

    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")
        self.assertEqual(b.to_json_string([]), "[]")
        self.assertEqual(b.to_json_string([{'id': 1, 'x': 2, 'y': 3,
                                            'width': 4, 'height': 5}]),
                         '[{"id": 1, "x": 2, "y": 3,"width": 4, "height": 5}]')

    def test_save_to_file(self):
        b = Base()
        b.save_to_file(None)
        with open("Base.json", mode="r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        b.save_to_file([])
        with open("Base.json", mode="r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        b.save_to_file([{'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}])
        with open("Base.json", mode="r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string(self):
        b = Base()
        self.assertEqual(b.from_json_string(None), [])
        self.assertEqual(b.from_json_string(""), [])
        self.assertEqual(b.from_json_string(
            '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'),
            [{'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}])

    def test_create(self):
        b = Base()
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        r = b.create(**d)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

    def test_load_from_file(self):
        b = Base()
        r = b.load_from_file()
        self.assertEqual(r, [])

        with open("Base.json", mode="w", encoding="utf-8") as f:
            f.write('[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]')

        r = b.load_from_file()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].id, 1)
        self.assertEqual(r[0].x, 2)
        self.assertEqual(r[0].y, 3)
        self.assertEqual(r[0].width, 4)
        self.assertEqual(r[0].height, 5)
