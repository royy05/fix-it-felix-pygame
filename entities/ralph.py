
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
    MIN_BROKEN_WINDOWS,
    MAX_BROKEN_WINDOWS,
)


class RalphState(Enum):
    CLIMBING = auto()
    MOVING = auto()
    ATTACKING = auto()
    INTRO_FINISHED = auto()


class Ralph(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        # State
        self._state = RalphState.CLIMBING

        # Movement
        self._move_speed = 100.0
        self._direction = 1
        self._target_x = x
        self._target_y = y

        # Introduction
        self._broken_windows = set()
        
        #which to destroy
        self._windows_to_destroy = set()
        
        #how many windows to break
        self._windows_to_break = 8
        
        
        self._climb_timer = 0.0
        self._climb_interval = 0.0

        # Rooftop movement
        self._move_timer = 0.0
        self._move_interval = 0.0

        # Attacking
        self._attack_timer = 0.0
        self._attack_interval = 2.5
        self._debris_speed = 120.0
        
        self._current_window_index = 0 #tracks which window Ralph is currently visiting
        

    def start_intro(self, building):
        """Prepare Ralph's introduction by selecting which window he will destroy during his five-second climb."""
        
        #resetting for new game
        self._state = RalphState.CLIMBING
        self._climb_timer = 0.0
        self._current_window_index = 0
        self._broken_windows.clear()
        self._windows_to_destroy.clear()
        
        
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
        
    def climb(self, dt, building): #BuildingObject
        """Move Ralph floor by floor and destroy selected windows."""
        self._climb_timer += dt
        
        #sort windows by floor number, then window number
        sorted_windows = sorted(
            self._windows_to_destroy,
            key = lambda window: (window[0], window[1])
        ) 

        if self._current_window_index < len(sorted_windows):
            current_window = sorted_windows[self._current_window_index] 
            floor_num, window_num = current_window   #tuple unpacking
            
            target_window = None
            for target in building.windows:
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
                
                self.destroy_window(building, floor_num, window_num)
                self._current_window_index += 1
                
            elif distance > 0:   
                dx /= distance
                dy /= distance
            
                #Ralph position update with overshooting problem prevention

                self._x += step * dx 
                self._y += step * dy

                      
    def destroy_window(self, building, floor_number, window_number):
        """Request Building to break a selected window and record it to the broken window set."""
        building.break_window(floor_number, window_number)
        self._broken_windows.add((floor_number, window_number))

    def finish_intro(self):
        """Finish the introduction and prepare rooftop gameplay."""
        self._state = RalphState.INTRO_FINISHED
        self._move_timer = 0.0
        self._attack_timer = 0.0
        #to be continued after building is finished

    def move_rooftop(self, dt):
        """Move Ralph horizontally between rooftop positions."""
        pass

    def attack(self):
        """Create a random number of bricks during an attack."""
        pass

    def set_attack_parameters(self, spawn_interval, debris_speed):
        """Receive current difficulty settings from PlayingState."""
        self._attack_interval = spawn_interval
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
        pass

    def draw(self, screen):
        """Draw Ralph."""
        pass
