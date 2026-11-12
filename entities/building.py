"""Building layout, window ownership and window management."""

import random
import pygame

from config import (
    TOTAL_FLOORS,
    WINDOWS_PER_FLOOR,
    MIN_BROKEN_WINDOWS,
    MAX_BROKEN_WINDOWS,
)
from entities.window import Window


class Building:
    def init(self):
        self._floors = TOTAL_FLOORS
        self._windows_per_floor = WINDOWS_PER_FLOOR
        self._windows = []
        self._broken_window_count = 0

        self.create_windows()
        
    @property
    def windows(self):
        return tuple(self._windows)

    def create_windows(self):
        """Create all windows and assign their positions."""
        pass

    def break_window(self, floor_number, window_number):
        """Break a specific window when requested by Ralph."""
        pass

    def generate_broken_windows(self):
        """Randomly break 6–12 windows, at least one on each floor."""
        pass

    def get_broken_windows(self):
        """Return all currently broken windows."""
        pass

    def get_repaired_count(self):
        """Return the number of fully repaired windows."""
        pass

    def all_windows_repaired(self):
        """Check whether all broken windows have been repaired."""
        pass

    def update(self, dt):
        """Update all window objects."""
        pass

    def draw(self, screen):
        """Draw building structure and its windows."""
        pass