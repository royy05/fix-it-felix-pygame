"""Player-controlled Felix."""

import pygame

from config import MAX_LIVES, PLAYER_INVULNERABILITY_TIME
from entities.game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, image=None):
        super().__init__(x, y, width, height, image)
        self._speed = 0.0
        self._lives = MAX_LIVES
        self._invulnerability_timer = 0.0
        self._is_invulnerable = False

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value < 0:
            raise ValueError("Lives cannot be negative")

        self._lives = value

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
