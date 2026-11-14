
"""Ralph's introduction, rooftop movement and debris attacks."""

import random
import pygame
from enum import Enum, auto
import math

from entities.game_object import GameObject
from entities.brick import Brick

from config import (
    BRICK_SIZE,
    TOTAL_FLOORS,
    WINDOWS_PER_FLOOR,
    BROKEN_WINDOWS
)

class RalphState(Enum):
    CLIMBING = auto()
    MOVING = auto()
    ATTACKING = auto()

class Ralph(GameObject):
    def __init__(self, x, y, width, height, building):
        super().__init__(x, y, width, height)

        # State
        self._state = RalphState.CLIMBING

        # Movement
        self._move_speed = 100.0
        self._direction = 1
        self._target_x = x
        self._target_y = y

        self._building = building
        # Introduction
        self._broken_windows = set()
        
        #which to destroy
        self._windows_to_destroy = set()
        
        #how many windows to break
        self._windows_to_break = BROKEN_WINDOWS

        # Rooftop movement
        self._move_timer = 0.0
        self._move_interval = 0.0
        
        # Attacking
        self._attack_timer = 0.0
        self._debris_speed = 120.0
        self._attack_duration = 0.8
        
        self._attack_performed = False #brick hasn't been dropped
        
        self._current_window_index = 0 #tracks which window Ralph is currently visiting
        self._sorted_windows_to_destroy = []
        
        # Load images
        self._idle_image = pygame.image.load("assets/images/characters/ralph/ralph_idle.png").convert_alpha()
        self._throw_image = pygame.image.load("assets/images/characters/ralph/ralph_throw.png").convert_alpha()

        # Scale images
        self._idle_image = pygame.transform.scale(
            self._idle_image, (self._width, self._height)
        )

        self._throw_image = pygame.transform.scale(
            self._throw_image, (self._width, self._height)
        )

        # Current image show as idle
        self._image = self._idle_image

    @property
    def is_climbing(self):
        return self._state == RalphState.CLIMBING
    
    def start_intro(self):
        """Prepare Ralph's introduction by selecting which window he will destroy while climbing."""
        
        #resetting for new game
        self._state = RalphState.CLIMBING
        self._attack_timer = 0.0
        self._move_timer = 0.0
        self._attack_performed = False
        
        self._x = self._building.roof_left
        self._y = self._building.building_bottom - self._height #start from the bottom
        self._direction = 1
        
        self._current_window_index = 0
        self._broken_windows.clear()
        self._windows_to_destroy.clear()
        self._sorted_windows_to_destroy.clear()
        
        #generate all 16 possible window positions so Ralph can randomly choose which to destroy
        available_windows = []
        for floor in range(TOTAL_FLOORS):
            for window in range(WINDOWS_PER_FLOOR):
                window_pair = (floor, window) #tuple
                available_windows.append(window_pair)
        
        #select at least one window from every floor
        for floor in range(TOTAL_FLOORS):
            floor_windows =[
                window for window in available_windows
                if window[0] == floor
            ]
            selected_window = random.choice(floor_windows)
            self._windows_to_destroy.add(selected_window)
            
        #select the remaining windows
        current_count = len(self._windows_to_destroy)
        remaining = self._windows_to_break - current_count
        remaining_windows = [
            window for window in available_windows
            if window not in self._windows_to_destroy
        ]
        
        extra_windows = random.sample(remaining_windows, remaining)
        self._windows_to_destroy.update(extra_windows)
        
        self._sorted_windows_to_destroy = sorted(
            self._windows_to_destroy,
            key=lambda window: (window[0], window[1])
        )
        
    def climb(self, dt): 
        """Move Ralph floor by floor and destroy selected windows."""


        if self._current_window_index < len(self._sorted_windows_to_destroy):
            current_window = self._sorted_windows_to_destroy[self._current_window_index] 
            floor_num, window_num = current_window   #tuple unpacking
            
            target_window = None
            for target in self._building.windows:
                if target.floor_number == floor_num and target.window_number == window_num: #Encapsulation
                    target_window = target
                    break    #stop the loop as soon as we find first matching window
                
            if target_window is None:
                raise ValueError("valid target window must exist as all 16 windows have been initialized in building object.") 
            
            #Ralph will be standing slightly to the left, and center of the window    
            self._target_x = target_window.x - 20
            self._target_y = target_window.y + (target_window.height / 2) - (self._height / 2)
            
            dx = self._target_x - self._x
            dy = self._target_y - self._y
            distance = math.hypot(dx, dy)
                
            step = dt * self._move_speed #total distance Ralph can travel per frame
            
            if distance <= step:
                self._x = self._target_x
                self._y = self._target_y
                
                self.destroy_window(floor_num, window_num)
                self._current_window_index += 1
                
            elif distance > 0:   
                dx /= distance
                dy /= distance
            
                #Ralph position update with overshooting problem prevention
                self._x += step * dx 
                self._y += step * dy

                      
    def destroy_window(self, floor_number, window_number):
        """Request Building to break a selected window and record it to the broken window set."""
        self._building.break_window(floor_number, window_number)
        self._broken_windows.add((floor_number, window_number))

    def finish_intro(self):
        """Finish the introduction and prepare rooftop gameplay."""
        self._move_timer = 0.0
        self._attack_timer = 0.0
        
        self._x = self._building.roof_left
        self._y = self._building.roof_y - self._height

        self._state = RalphState.MOVING
        self._direction = 1
        self._attack_performed = False
        
    def move_rooftop(self, dt):
        """Move Ralph horizontally between rooftop positions."""

        left_limit = self._building.roof_left
        right_limit = self._building.roof_right - self._width
        
        self._x += self._direction * dt * self._move_speed
        if self._x >= right_limit:
            self._x = right_limit
            self._direction = -1
            
        elif self._x <= left_limit:
            self._x = left_limit
            self._direction = 1
            

    def attack(self):
        """Create a random number of bricks during an attack."""
        brick_number = random.randint(1, 3)
        brick_list = []
        
        for _ in range(brick_number):
            brick = self.drop_debris()
            brick_list.append(brick)
            
        return brick_list
        
            
    def set_attack_parameters(self, spawn_interval, debris_speed):
        """Receive current difficulty settings from PlayingState."""
        self._move_interval = spawn_interval
        self._debris_speed = debris_speed

    def drop_debris(self):
        """Create and return a new Brick object."""
        brick_width, brick_height = BRICK_SIZE
        brick = Brick(self._x,
                      self._y,
                      brick_width,
                      brick_height,
                      self._debris_speed)
        return brick

    def update(self, dt):
        """Update Ralph according to his current state."""
        
        #state-based animation, switching between throw and idle
        if self._state == RalphState.ATTACKING:
            self._image = self._throw_image
        else:
            self._image = self._idle_image
        
        new_bricks =[]
        if self._state == RalphState.CLIMBING:
            
            self.climb(dt) #starting state is climbing
            
            if self._current_window_index >= len(self._sorted_windows_to_destroy):
                self.finish_intro()
        
        elif self._state == RalphState.MOVING:
            self._move_timer += dt
            
            if self._move_timer < self._move_interval:
                self.move_rooftop(dt)
            else:
                self._state = RalphState.ATTACKING
                self._attack_timer = 0.0
        
        elif self._state == RalphState.ATTACKING:
            self._attack_timer += dt
            
            if not self._attack_performed:
                new_bricks = self.attack()
                self._attack_performed = True
                
                 
            if self._attack_timer >= self._attack_duration:
                self._state = RalphState.MOVING
                self._move_timer = 0.0
                self._attack_timer = 0.0
                self._attack_performed = False
                
        return new_bricks
                

    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))   # parameters => (source, destination)
        
        # note: (self.x, self.y) as destination so we can draw ralph at his position
