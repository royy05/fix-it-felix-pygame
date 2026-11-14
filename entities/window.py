"""Individual building window and its repair state."""

import pygame
import os

from entities.game_object import GameObject
from config import (
    REPAIRS_REQUIRED
)

class Window(GameObject):  # inherits from GameObject
    
    _image_cache = {}
    
    def __init__(self, x, y, width, height, floor_number, window_number,
                 is_broken=False):
        super().__init__(x, y, width, height)
        self._floor_number = floor_number
        self._window_number = window_number
        self._is_broken = is_broken
        self._repair_progress = 0
        self._required_repairs = REPAIRS_REQUIRED
        
        # so window can retrieve the shared images
        image_size = (width, height)
        
        if image_size not in Window._image_cache:
            
            # loading images from assets
            asset_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "assets",
                "images",
                "windows"
            )

            # Load window images
            fixed_path = os.path.join(
                asset_path, "window_fixed.png"
            )

            broken_path = os.path.join(
                asset_path, "window_broken.png"
            )

            fixed_image = pygame.image.load(
                fixed_path
            ).convert_alpha()

            broken_image = pygame.image.load(
                broken_path
            ).convert_alpha()

            # Scale images to match the window dimensions
            fixed_image = pygame.transform.scale(
                fixed_image, image_size
            )

            broken_image = pygame.transform.scale(
                broken_image, image_size
            )
            
            Window._image_cache[image_size] = (
                fixed_image, broken_image
            )
            
        self._fixed_image, self._broken_image = (
            Window._image_cache[image_size]
        )
        
        
    # concept here :
    # encapsulation: each object controlling its own internal data and
    # gives methods through which other obj can interact with it.
    # like fixing window 1 will not affect the state of window 2 or 3.
    # cuz we need to press space 3 time to have a fixed window state.
    
    @property
    def floor_number(self):
        return self._floor_number
    
    #concept: property allows other classes to access information
    # while preserving encapsulation.

    @property
    def window_number(self):
        return self._window_number
    
    @property
    def repair_progress(self):
        return self._repair_progress
    
    @property
    def is_broken(self): # for other classes to check whether the window is broken
        return self._is_broken
    
    def break_window(self):
        # called by Building when Ralph reaches a selected window
        # in Ralph.py >> building.break_window(floor_number, window_number)    
        # for : mark the window as broken
        if not self._is_broken:
            self._is_broken = True
            self._repair_progress = 0

#ABOUT repair() and is_repaired()
# repair ==> perform repair--> increase repair progress (pressing space 3 times) action
# is_repaired ==> check result/ condition to tell other classes whether the window is repaired

    def repair(self):
        # if broken, increase repair progress. check repair progress == 3 then window is repaired.
        # if not broken, do noting.
        if self._is_broken == True:
            self._repair_progress += 1
            
            if self._repair_progress >= self._required_repairs:
                self._is_broken = False
                return True  # repaired now
            else:
                return False # still broken
            
        else:
            return False #window not broken in the first place, so repaired is false. No repairs needed.
        
    def is_repaired(self):
        """Check whether the window has been fully repaired."""
        # check if window is still broken and repair is complete
        if self._is_broken == False:
            if self._repair_progress >= self._required_repairs:
                return True
            else:
                return False
        else:
            return False
        

    def update(self, dt):
        # dt = amount of time passed since the previous frame (delta time)
        """Update window animation or visual effects."""
        pass
        

    def draw(self, screen):
        """Draw the window according to its current condition."""
        if self._is_broken:
            screen.blit(self._broken_image, (self.x, self.y))
            
        else:
            screen.blit(self._fixed_image, (self.x, self.y))
            
# self.x , self.y position attributes were able to use cuz of inheritance from gameobject
