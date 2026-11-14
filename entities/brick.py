"""Falling debris dropped by Ralph."""

import pygame
import os

from entities.game_object import GameObject
from config import SCREEN_HEIGHT

class Brick(GameObject):
    
    _image_cache = {} # class attribute
    # all Brick objects sharing the same dictionary
    # so that the existing image is retrieved after it has been loaded and scaled for the first time
    # because the bricks will keep falling so need to avoid loading repeatedly
    
    def __init__(self, x, y, width, height, fall_speed):
        super().__init__(x, y, width, height)
        self._fall_speed = fall_speed
        self._is_active = True
        self._has_hit_player = False
        
        # load brick image if it hasn't been loaded before.
        image_size = (width, height)
        
        if image_size not in Brick._image_cache:
            
            asset_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "assets",
                "images",
                "objects"
            )

            brick_path = os.path.join(
                asset_path, "brick.png"
            )
            
            # load
            image = pygame.image.load(
                brick_path
            ).convert_alpha()

            # Scale image to match the brick dimensions.
            image = pygame.transform.scale(
                image, image_size
            )

            Brick._image_cache[image_size] = image

        self._image = Brick._image_cache[image_size]
        
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

    def update(self, dt):
        self.fall(dt)

        if self._y + self._height > SCREEN_HEIGHT:
            self._is_active = False

    def draw(self, screen):
        # draw the falling brick image
        
        screen.blit(
            self._image,
            (self._x, self._y)
        )






   