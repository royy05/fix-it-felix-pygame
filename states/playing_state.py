"""Active gameplay state and gameplay coordinator."""

import pygame

from config import (
    INTRO_DELAY,
    GAME_DURATION,
    EASY_END,
    MEDIUM_END,
    EASY_DEBRIS_SPEED,
    MEDIUM_DEBRIS_SPEED,
    HARD_DEBRIS_SPEED,
    EASY_SPAWN_INTERVAL,
    MEDIUM_SPAWN_INTERVAL,
    HARD_SPAWN_INTERVAL,
)
from states.game_state import GameState
from entities.building import Building
from entities.player import Player
from entities.ralph import Ralph
from states.win_state import WinState
from states.lose_state import LoseState

class PlayingState(GameState):
    def __init__(self, game_manager):
        super().__init__(game_manager)
        self._building = None 
        self._player = None 
        self._ralph = None
        self._debris = []
        self._entities = []

        self._intro_timer = 0.0
        self._game_started = False
        self._elapsed_time = 0.0
        self._remaining_time = GAME_DURATION

    def enter(self):
        """Initialize or reset the gameplay environment whenever PlayingState becomes active."""
        #in order to prevent previous playing state's objects (before restarting) still active after restart,
        #we decided to initialize here. so all objects will be new when the PlayingState is active again.
        pass

    def handle_events(self, events):
        """Handle movement and SPACE repair input."""
        pass

    def update(self, dt):
        """Update introduction, timer, difficulty and game objects."""
        pass

    def draw(self, screen):
        """Draw building, entities and gameplay HUD."""
        pass

    def exit(self):
        pass

    def update_difficulty(self):
        """Choose debris speed and spawn interval from elapsed time."""
        if self._elapsed_time < EASY_END:
            debris_speed = EASY_DEBRIS_SPEED
            spawn_interval = EASY_SPAWN_INTERVAL
        elif self._elapsed_time < MEDIUM_END:
            debris_speed = MEDIUM_DEBRIS_SPEED
            spawn_interval = MEDIUM_SPAWN_INTERVAL
        else:
            debris_speed = HARD_DEBRIS_SPEED
            spawn_interval = HARD_SPAWN_INTERVAL
            
        self._ralph.set_attack_parameters(spawn_interval, debris_speed)

    def spawn_debris(self, dt):
        """Ask Ralph to create debris and add it to the active collection."""
        pass

    def handle_collisions(self):
        """Check debris/player collisions and remove inactive debris."""
        pass

    def check_win_condition(self):
        if self._building.all_windows_repaired() and self._player.lives >=1:
            self._game_manager.change_state(WinState(self._game_manager))

    def check_lose_condition(self):
        if self._player.lives == 0 or (
            self._remaining_time <= 0 and not self._building.all_windows_repaired()
            ):
            self._game_manager.change_state(LoseState(self._game_manager))

    def _find_repair_target(self):
        """Return the eligible nearby broken window, if any."""
        pass

    def _update_entity_collection(self, dt):
        """Demonstrate polymorphic update dispatch."""
        pass
    
    def _draw_entity_collection(self, screen):
        """Demonstrate polymorphic draw dispatch."""
        for entity in self._entities:
            entity.draw(screen)
