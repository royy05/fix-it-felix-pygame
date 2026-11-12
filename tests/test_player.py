"""Tests for Player lives and damage behaviour."""

import unittest

from entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(0, 0, 40, 60)

    def test_player_starts_with_three_lives(self):
        pass

    def test_damage_reduces_lives(self):
        pass

    def test_lives_validation(self):
        pass


if __name__ == "__main__":
    unittest.main()
