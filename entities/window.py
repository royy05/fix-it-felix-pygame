"""Individual building window and its repair state."""

from entities.game_object import GameObject


class Window(GameObject):
    def init(self, x, y, width, height, floor_number, window_number,
                 is_broken=False):
        super().init(x, y, width, height)

        self._floor_number = floor_number
        self._window_number = window_number
        self._is_broken = is_broken
        self._repair_progress = 0
        self._required_repairs = 3

    @property
    def floor_number(self):
        return self._floor_number

    @property
    def window_number(self):
        return self._window_number

    @property
    def repair_progress(self):
        return self._repair_progress

    @property
    def is_broken(self):
        return self._is_broken

    def break_window(self):
        """Break the window during Ralph's introduction."""
        pass

    def repair(self):
        """Register one valid repair press."""
        pass

    def is_repaired(self):
        """Check whether the window has been fully repaired."""
        pass

    def update(self, dt):
        """Update window animation or visual effects."""
        pass

    def draw(self, screen):
        """Draw the window according to its current condition."""
        pass