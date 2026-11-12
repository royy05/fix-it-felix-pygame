"""Tests for Building window generation."""

import unittest

from entities.building import Building


class TestBuilding(unittest.TestCase):
    def setUp(self):
        self.building = Building()

    def test_creates_sixteen_windows(self):
        pass

    def test_broken_window_count_is_in_range(self):
        pass

    def test_each_floor_has_a_broken_window(self):
        pass


if __name__ == "__main__":
    unittest.main()
