"""Player-controlled Felix."""

import pygame
import math
from config import MAX_LIVES, PLAYER_INVULNERABILITY_TIME, FELIX_SPEED, PLAY_AREA, FIX_RANGE, FIX_TIME
from entities.game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, image=None):
        super().__init__(x, y, width, height) #push: remove image
        self._speed = FELIX_SPEED
        self._lives = MAX_LIVES
        self._invulnerability_timer = 0.0
        self._is_invulnerable = False

        self._repair_timer = 0.0
        self._is_repairing = False
        self._repair_target = None

        self._idle_image = pygame.image.load(
            "assets/images/characters/felix/felix_idle.png"
        ).convert_alpha()

        self._fix_image = pygame.image.load(
            "assets/images/characters/felix/felix_fix.png"
        ).convert_alpha()

        self._hurt_image = pygame.image.load(
            "assets/images/characters/felix/felix_hurt.png"
        ).convert_alpha()

        self._idle_image = pygame.transform.scale(
            self._idle_image,(width,height)
        )

        self._fix_image = pygame.transform.scale(
            self._fix_image, (width,height)
        )

        self._hurt_image = pygame.transform.scale(
            self._hurt_image, (width,height)
        )

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value < 0:
            raise ValueError("Lives cannot be negative")

        self._lives = value

    def move(self, direction, dt):
        if direction == "left":
            self._x -= self._speed * dt

        elif direction == "right":
            self._x += self._speed * dt

        elif direction == "up":
            self._y -= self._speed * dt

        elif direction == "down":
            self._y += self._speed * dt

        left, top, area_width, area_height = PLAY_AREA
        right = left + area_width
        bottom = top + area_height


        if self._x < left:
            self._x = left

        if self._x + self._width > right:
            self._x = right - self._width

        if self._y < top:
            self._y = top

        if self._y + self._height > bottom:
            self._y = bottom - self._height
    

    def take_damage(self):
        if self._is_invulnerable:
            return False

        self._lives -= 1

        self._is_invulnerable = True
        self._invulnerability_timer = PLAYER_INVULNERABILITY_TIME

        return True

    def repair_window(self, window):
        if self._is_repairing:
            return

        if not window.is_broken:
            return

        player_center_x = self._x + self._width / 2
        player_center_y = self._y + self._height / 2


        window_rect = window.get_rect()
        window_center_x, window_center_y = window_rect.center

        distance = math.hypot(
            player_center_x - window_center_x,
            player_center_y - window_center_y
        )

        if distance > FIX_RANGE:
            return

       

        self._repair_timer = FIX_TIME
        self._is_repairing = True
        self._repair_target = window


        
        

    def update(self, dt):
        if self._is_invulnerable:
            self._invulnerability_timer -= dt

            if self._invulnerability_timer <= 0:
                self._invulnerability_timer = 0
                self._is_invulnerable = False

        if self._is_repairing:
            self._repair_timer -= dt

            if self._repair_timer <= 0:
                if self._repair_target is not None:
                  self._repair_target.repair()
                self._repair_timer = 0.0
                self._is_repairing = False
                self._repair_target = None



        

    def draw(self, screen):
        if self._is_invulnerable:
            image = self._hurt_image

        elif self._is_repairing:
            image = self._fix_image

        else:
            image = self._idle_image

        screen.blit(image,(self._x,self._y))
