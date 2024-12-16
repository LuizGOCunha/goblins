from libraries.map import Map
from libraries.wall import Wall
from unittest import TestCase


class MapTest(TestCase):
    """Tests for the Map object"""
    def setUp(self):
        self.map = Map()

    def test_get_object_in_position(self):
        self.assertEqual(self.map.get_object_in_position(-1, 0), Wall)
        self.assertEqual(self.map.get_object_in_position(0, -1), Wall)
        self.assertEqual(self.map.get_object_in_position(self.map.X_SIZE + 1, 1), Wall)
        self.assertEqual(self.map.get_object_in_position(1, self.map.X_SIZE + 1), Wall)

    def test_get_object_in_position_returns_object_if_within_bounds(self):
        obj = "TestObject"
        self.map.add_object_in_position(obj, 2, 3)
        self.assertEqual(self.map.get_object_in_position(2, 3), obj)

    def test_add_object_in_position_adds_object(self):
        obj = "AnotherObject"
        self.map.add_object_in_position(obj, 4, 5)
        self.assertEqual(self.map.grid[5][4], obj)

    def test_empty_position_removes_object(self):
        obj = "RemovableObject"
        self.map.add_object_in_position(obj, 1, 1)
        self.map.empty_position(1, 1)
        self.assertIsNone(self.map.get_object_in_position(1, 1))

    def test_validate_coordinates_returns_valid_coordinates(self):
        coordinates = [(1, 1), (11, 5), (5, -1), (3, 3)]
        expected = [(1, 1), (3, 3)]
        self.assertEqual(self.map.validate_coordinates(coordinates), expected)

    def test_validate_coordinates_excludes_invalid_coordinates(self):
        coordinates = [(-1, 0), (0, -1), (self.map.X_SIZE + 1, 0), (0, self.map.Y_SIZE + 1)]
        expected = []
        self.assertEqual(self.map.validate_coordinates(coordinates), expected)
