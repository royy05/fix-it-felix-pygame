"""Player-controlled Felix."""

import pygame

from config import TOTAL_LIVES, PLAYER_INVULNERABILITY_TIME
from entities.game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, image=None):
        super().__init__(x, y, width, height, image)
        self._speed = 0.0
        self._lives = TOTAL_LIVES
        self._invulnerability_timer = 0.0
        self._is_invulnerable = False

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        pass

    def move(self, direction, dt):
        pass

    def take_damage(self):
        pass

    def repair_window(self, window):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass
