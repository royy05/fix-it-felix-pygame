"""Abstract base class for physical game objects."""
# parent class -- position, width n height, get_rect(), common obj functionalities
# player - ralph - window - brick

from abc import ABC, abstractmethod
import pygame

class GameObject(ABC):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    # every class inheriting gameobject must have these two methods:
    # update and draw
    @abstractmethod
    def update(self, dt):
        """Update this object's state."""
        pass

    @abstractmethod
    def draw(self, screen):
        """Draw this object on the screen."""
        pass

    def get_rect(self):
        """Return this object's collision rectangle."""
        return pygame.Rect(self._x, self._y, self._width, self._height)
        # rectangle representing object position and size
        # for felix and brick collision - damage taken

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height