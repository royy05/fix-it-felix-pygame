"""Falling debris dropped by Ralph."""

import pygame

from entities.game_object import GameObject


class Brick(GameObject):
    def __init__(self, x, y, width, height, fall_speed):
        super().__init__(x, y, width, height)
        self._fall_speed = fall_speed
        self._is_active = True
        self._has_hit_player = False

    def fall(self, dt):
        pass

    def check_collision(self, player):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass
