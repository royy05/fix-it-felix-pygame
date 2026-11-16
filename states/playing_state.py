"""Active gameplay state and gameplay coordinator."""

import pygame
import math
import os

from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    GAME_DURATION,
    EASY_END,
    MEDIUM_END,
    EASY_DEBRIS_SPEED,
    MEDIUM_DEBRIS_SPEED,
    HARD_DEBRIS_SPEED,
    EASY_SPAWN_INTERVAL,
    MEDIUM_SPAWN_INTERVAL,
    HARD_SPAWN_INTERVAL,
    FELIX_SIZE,
    RALPH_SIZE,
    PLAY_AREA,
    GROUND_Y,
    FIX_RANGE
)
from states.game_state import GameState
from entities.building import Building
from entities.player import Player
from entities.ralph import Ralph
from states.win_state import WinState
from states.lose_state import LoseState
from events import GAME_WON, GAME_LOST

class PlayingState(GameState):
    def __init__(self, game_manager):
        super().__init__(game_manager)
        self._building = None 
        self._player = None 
        self._ralph = None
        self._debris = []
        self._entities = []

        self._game_started = False #Felix can be controlled 
        self._felix_entering = False #Felix walking into the scene
        self._felix_target_x = 0 #where Felix should stop
        
        self._elapsed_time = 0.0
        self._remaining_time = GAME_DURATION

        self._hud_font = pygame.font.Font(None, 32)
        
    def enter(self):
        """Initialize or reset the gameplay environment whenever PlayingState becomes active."""
        #in order to prevent previous playing state's objects (before restarting) still active after restart,
        #we decided to initialize here. so all objects will be new when the PlayingState is active again.
        #create a fresh building
        
        asset_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "assets",
            "images",
            "background",
            "background.png"
        )
        
        self._background = pygame.image.load(
            asset_path
        ).convert()
        
        self._background = pygame.transform.scale(
            self._background,
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        
        self._building = Building()
        
        #create felix
        felix_width, felix_height = FELIX_SIZE
        felix_x = - felix_width
        felix_y = GROUND_Y - felix_height
        self._player = Player(
            felix_x,
            felix_y,
            felix_width, 
            felix_height
        )
        
        #Felix's final entrance position
        self._felix_target_x = PLAY_AREA[0] + 10
        self._felix_entering = False
        
        #create Ralph
        ralph_width, ralph_height = RALPH_SIZE
        ralph_x = self._building.roof_left
        ralph_y = self._building.roof_y - ralph_height
        
        self._ralph = Ralph(
            ralph_x,
            ralph_y,
            ralph_width,
            ralph_height,
            self._building
        )
        self._ralph.start_intro()
        # Initialize object collections
        self._debris = []

        self._entities = [
            self._building,
            self._player,
            self._ralph
        ]
        
        # Reset gameplay timers
        self._game_started = False
        self._felix_entering = False
        self._elapsed_time = 0.0
        self._remaining_time = GAME_DURATION
        
        self.update_difficulty()
        self._game_manager._sound_manager.play_music("background")
        
    def handle_events(self, events):
        """Handle keyboard events for window repair."""
        if not self._game_started:
            return
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window = self._find_repair_target()
                    
                    if window is not None:
                        self._player.repair_window(window)
                        
    def handle_player_movement(self, dt):
        """Handle keyboard input and move Felix in one direction at a time."""
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self._player.move("left", dt)
        
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self._player.move("right", dt)
        
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self._player.move("up", dt)
        
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self._player.move("down", dt)
            
    def update(self, dt):
        """Update introduction, timer, difficulty and game objects."""

        #Update Building and Player
        self.update_entity_collection(dt)

        #Update Ralph and collect new bricks
        self.spawn_debris(dt)

        #Update falling bricks
        for brick in self._debris:
            brick.update(dt)

        #Start Felix's entrance after Ralph finishes climbing
        if not self._game_started and not self._felix_entering:
            if not self._ralph.is_climbing:
                self._felix_entering = True
        #Move Felix into the scene
        if self._felix_entering:
            arrived = self._player.enter_scene(
                dt,
                self._felix_target_x
            )
            if arrived:
                self._felix_entering = False
                self._game_started = True
                
        #Update gameplay timer and difficulty
        if self._game_started:
            
            self.handle_player_movement(dt)
            self._elapsed_time += dt
            self._remaining_time = max(0, GAME_DURATION - self._elapsed_time)
            self.update_difficulty()

        #Handle collisions
        self.handle_collisions()


        #Check game-ending conditions
        self.check_win_condition()
        
        #check whether the current state is still PlayingState
        if self._game_manager.current_state is self: 
            self.check_lose_condition()
        
    def draw(self, screen):
        """Draw building, entities and gameplay HUD."""
        
        screen.blit(self._background, (0,0))
        
        self._draw_entity_collection(screen)
        self._draw_debris(screen)

        if self._game_started:
            self.draw_hud(screen) #will appear only after Felix becomes controllable
            
    def exit(self):
        
        self._building = None
        self._player = None
        self._ralph = None
        self._debris.clear()
        self._entities.clear()
        self._game_manager._sound_manager.stop_music()

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

    def spawn_debris(self,dt):
        """Add Ralph's newly created bricks to _debris."""
        new_bricks = self._ralph.update(dt)
        self._debris.extend(new_bricks)
        
    def handle_collisions(self):
        """Check debris/player collisions and remove inactive debris."""
        for brick in self._debris:
            brick.check_collision(self._player)
        self._debris = [brick for brick in self._debris if brick.is_active]

    def check_win_condition(self):
        if self._building.all_windows_repaired() and self._player.lives >=1:
            pygame.event.post(
                pygame.event.Event(GAME_WON)
            )
            self._game_manager.change_state(WinState(self._game_manager))

    def check_lose_condition(self):
        if self._player.lives == 0 or (
            self._remaining_time <= 0 and not self._building.all_windows_repaired()
            ):
            pygame.event.post(
                pygame.event.Event(GAME_LOST)
            )
            self._game_manager.change_state(LoseState(self._game_manager))

    def _find_repair_target(self):
        """Return the eligible nearby broken window, if any."""
       
        nearest_window = None
        nearest_distance = float("inf")

        # Calculate the centre of Felix
        player_center_x = self._player.x + self._player.width / 2
        player_center_y = self._player.y + self._player.height / 2
        
        # Check every window in the building
        for window in self._building.windows:

            # Ignore windows that are not broken
            if not window.is_broken:
                continue

            # Calculate the centre of the window
            window_center_x = window.x + window.width / 2
            window_center_y = window.y + window.height / 2

            # Calculate distance between Felix and the window
            distance = math.hypot(
                window_center_x - player_center_x,
                window_center_y - player_center_y
            )

            # Keep the nearest window within repair range
            if distance <= FIX_RANGE and distance < nearest_distance:
                nearest_distance = distance 
                nearest_window = window

        return nearest_window

    def update_entity_collection(self, dt):
        for entity in self._entities:
            if entity is not self._ralph: #avoid updating Ralph twice
                entity.update(dt)
    
    def _draw_entity_collection(self, screen):
        """Draw entities and show Felix during his entrance."""

        for entity in self._entities:
            if entity == self._player:
                if not self._game_started and not self._felix_entering:
                    continue

            entity.draw(screen)

    def _draw_debris(self, screen):
        """Draw all falling bricks."""
        for brick in self._debris:
            brick.draw(screen)
            
    def draw_hud(self, screen):
        """Display the timer, remaining lives and repair progress."""

        # -------------------------------
        # TIMER
        # -------------------------------

        minutes = int(self._remaining_time // 60)
        seconds = int(self._remaining_time % 60)

        timer_text = f"{minutes:02d}:{seconds:02d}"

        timer_surface = self._hud_font.render(
            timer_text, True, (255, 255, 255)
        )

        screen.blit(timer_surface, (20, 20))

        # -------------------------------
        # FELIX'S LIVES
        # -------------------------------

        lives_text = f"Lives: {self._player.lives}"

        lives_surface = self._hud_font.render(
            lives_text, True, (255, 255, 255)
        )

        screen.blit(lives_surface, (20, 60))

        # -------------------------------
        # REPAIR PROGRESS
        # -------------------------------

        repaired_count = self._building.get_repaired_count()
        total_broken = self._building.get_total_windows_to_repair()

        repair_text = f"Windows Repaired: {repaired_count}/{total_broken}"

        repair_surface = self._hud_font.render(
            repair_text, True, (255, 255, 255)
        )

        screen.blit(repair_surface, (20, 100))