"""Abstract base class for physical game objects."""

from abc import ABC, abstractmethod
import pygame


class GameObject(ABC):
    def __init__(self, x, y, width, height, image=None):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._image = image

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
        pass

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