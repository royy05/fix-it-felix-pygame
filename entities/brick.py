"""Falling debris dropped by Ralph."""

import pygame

from entities.game_object import GameObject
from config import SCREEN_HEIGHT
from events import PLAYER_DAMAGED

class Brick(GameObject):
    def __init__(self, x, y, width, height, fall_speed):
        super().__init__(x, y, width, height)
        self._fall_speed = fall_speed
        self._is_active = True
        self._has_hit_player = False

    @property
    def is_active(self):
        return self._is_active
    
    def fall(self, dt):
        self._y += self._fall_speed * dt

    def check_collision(self, player):
        if (self.get_rect().colliderect(player.get_rect())
                and not self._has_hit_player):

            if player.take_damage():
                self._has_hit_player = True

                pygame.event.post(
                    pygame.event.Event(PLAYER_DAMAGED)
                )

            

    def update(self, dt):
        self.fall(dt)

        if self._y + self._height > SCREEN_HEIGHT:
            self._is_active = False

    def draw(self, screen):
        if self._is_active:
            pygame.draw.rect(
                screen,
                (150, 60, 40),
                (
                    self._x,
                    self._y,
                    self._width,
                    self._height
                )
            )






   