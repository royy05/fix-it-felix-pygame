"""Tests for Window repair behaviour."""

import unittest

from entities.window import Window


class TestWindow(unittest.TestCase):
    def setUp(self):
        self.window = Window(0, 0, 50, 50, 1, 1, True)

    def test_one_press_increments_progress(self):
        pass

    def test_three_presses_repairs_window(self):
        pass

    def test_repaired_window_does_not_continue_progressing(self):
        pass


if __name__ == "__main__":
    unittest.main()
