
"""Building layout, roof, window ownership and drawing."""

import pygame

from config import (
    TOTAL_FLOORS,
    WINDOWS_PER_FLOOR,
    BUILDING_RECT,
    ROOF_SIZE,
    WINDOW_SIZE
)

from entities.window import Window


class Building:
    def __init__(self):
        """Initialize building, roof and all window objects."""

        self._floors = TOTAL_FLOORS
        self._windows_per_floor = WINDOWS_PER_FLOOR

        # Store all window objects.
        self._windows = []

        # ----------------------------------
        # BUILDING WALL
        # ----------------------------------

        self._building_image = pygame.image.load(
            "assets/images/objects/building_wall.png"
        ).convert_alpha()

        self._building_image = pygame.transform.scale(
            self._building_image,
            (BUILDING_RECT[2], BUILDING_RECT[3])
        )

        # ----------------------------------
        # ROOF
        # ----------------------------------

        self._roof_image = pygame.image.load(
            "assets/images/objects/roof.png"
        ).convert_alpha()

        self._roof_image = pygame.transform.scale(
            self._roof_image,
            ROOF_SIZE
        )

        building_x, building_y, building_width, building_height = BUILDING_RECT

        roof_width, roof_height = ROOF_SIZE

        # Centre roof horizontally above the building.
        roof_x = building_x + (building_width - roof_width) / 2

        # Position roof directly above the building wall.
        # top left corner of the roof image
        roof_y = building_y - roof_height

        self._roof_rect = pygame.Rect(
            roof_x,
            roof_y,
            roof_width,
            roof_height
        )

        # ----------------------------------
        # CREATE WINDOWS
        # ----------------------------------

        self.create_windows()

    # ======================================
    # PROPERTIES
    # ======================================

    @property
    def windows(self):
        """Return all windows as a read-only collection."""

        return tuple(self._windows)

    @property
    def roof_rect(self):
        """Return a copy of the roof rectangle."""

        return self._roof_rect.copy()

    @property
    def roof_center_x(self):
        """Return the horizontal centre of the roof."""

        return self._roof_rect.centerx

    @property
    def roof_y(self):
        """Return the top surface position of the roof."""

        return self._roof_rect.top

    @property
    def roof_left(self):
        """Return the left boundary of the roof."""

        return self._roof_rect.left

    @property
    def roof_right(self):
        """Return the right boundary of the roof."""

        return self._roof_rect.right

    # ======================================
    # WINDOW CREATION
    # ======================================

    def create_windows(self):
        """Create and position all windows in the building."""

        building_x, building_y, building_width, building_height = BUILDING_RECT

        window_width, window_height = WINDOW_SIZE

        # Calculate horizontal and vertical spacing.
        horizontal_spacing = (
            building_width - self._windows_per_floor * window_width
        ) / (self._windows_per_floor + 1)

        vertical_spacing = (
            building_height - self._floors * window_height
        ) / (self._floors + 1)

        horizontal_distance = window_width + horizontal_spacing
        vertical_distance = window_height + vertical_spacing

        # Create windows from top row to bottom row.
        for row in range(self._floors):

            # Reverse numbering:
            # Floor 0 = bottom floor
            # Floor 3 = top floor
            floor = self._floors - 1 - row

            for column in range(self._windows_per_floor):

                x = (
                    building_x
                    + horizontal_spacing
                    + column * horizontal_distance
                )

                y = (
                    building_y
                    + vertical_spacing
                    + row * vertical_distance
                )

                window = Window(
                    x,
                    y,
                    window_width,
                    window_height,
                    floor,
                    column,
                    False
                )

                self._windows.append(window)

    # ======================================
    # WINDOW MANAGEMENT
    # ======================================

    def break_window(self, floor_number, window_number):
        """Find and break the requested window."""

        for window in self._windows:

            if (
                window.floor_number == floor_number
                and window.window_number == window_number
            ):

                # Only break an intact window.
                if not window.is_broken:
                    window.break_window()

                return

        raise ValueError(
            f"Window not found: floor {floor_number}, "
            f"window {window_number}"
        )

    def get_broken_windows(self):
        """Return all currently broken windows."""

        return tuple(
            window
            for window in self._windows
            if window.is_broken
        )

    def all_windows_repaired(self):
        """Check whether all broken windows have been repaired."""

        return not self.get_broken_windows()

    # ======================================
    # UPDATE AND DRAW
    # ======================================

    def update(self, dt):
        """Update all window objects."""

        for window in self._windows:
            window.update(dt)

    def draw(self, screen):
        """Draw building wall, windows and roof."""

        # Draw building wall first.
        screen.blit(
            self._building_image,
            BUILDING_RECT[:2]
        )

        # Draw all windows on the building.
        for window in self._windows:
            window.draw(screen)

        # Draw roof last so it appears above the building.
        screen.blit(
            self._roof_image,
            self._roof_rect.topleft
        )
