"""Main menu state."""

import os
import pygame
import config as S

from states.game_state import GameState
from states.playing_state import PlayingState

class MenuState(GameState):
    def enter(self):
        """Initialise the menu state."""

        asset_path = os.path.join(os.path.dirname(__file__), "..", "assets")

        background_path = os.path.join(
            asset_path, "background", "background.png"
        )

        self._background = pygame.image.load(
            background_path
        ).convert()
        
        #scale
        self._background = pygame.transform.scale(
            self._background,
            (S.SCREEN_WIDTH, S.SCREEN_HEIGHT)
        )
        
        # button
                
        cx = S.SCREEN_WIDTH // 2

        self._button_width = 220
        self._button_height = 55

        self._start_button = pygame.Rect(
            cx - self._button_width // 2,
            390,
            self._button_width,
            self._button_height
        )

        self._quit_button = pygame.Rect(
            cx - self._button_width // 2,
            465,
            self._button_width,
            self._button_height
        )

        # Track which button the mouse is hovering over
        self._hovered_button = None

        # Initialize fonts

        self._title_font = pygame.font.Font(None, 100)
        self._subtitle_font = pygame.font.Font(None, 28)
        self._button_font = pygame.font.Font(None, 42)
        self._instruction_font = pygame.font.Font(None, 23)
        
        # creating overlay once
        self._overlay = pygame.Surface(
            (S.SCREEN_WIDTH, S.SCREEN_HEIGHT),
            pygame.SRCALPHA
        )

        self._overlay.fill((0, 0, 0, 120))

    def start_game(self):
        """Change from menu state to playing state."""

        self._game_manager.change_state(
            PlayingState(self._game_manager)
        )

    def handle_events(self, events):
        """ keyboard and mouse events"""
        
        for event in events:
                
            if event.type == pygame.KEYDOWN:
                
                # Press enter or space bar to START
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.start_game()
                
                # Press escape to QUIT
                elif event.key == pygame.K_ESCAPE:
                    self._game_manager.quit()
                    
                # Mouse click for button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    
                    if self._start_button.collidepoint(event.pos):
                        self.start_game()
                        
                    elif self._quit_button.collidepoint(event.pos):
                        self._game_manager.quit()
                        
            elif event.type == pygame.MOUSEMOTION:
                
                if self._start_button.collidepoint(event.pos):
                    self._hovered_button = "start"
                
                elif self._quit_button.collidepoint(event.pos):
                    self._hovered_button = "quit"
                    
                else:
                    self._hovered_button = None

    def update(self,dt):
        pass

    def draw(self, screen):
        # background
        screen.blit(self._background, (0,0))
        
        # dark transparent overlay
        screen.blit(self._overlay, (0,0))

        # draw game title
        cx = S.SCREEN_WIDTH // 2
        
        title1 = self._title_font.render(
            "FIX-IT", True, S.YELLOW
        )
        
        title2 = self._title_font.render(
            "FELIX", True, (90, 170, 255)
        )
        
        screen.blit(
            title1,
            title1.get_rect(center=(cx, 105))
        )
        
        screen.blit(
            title2,
            title2.get_rect(center=(cx,195))
        )
        
        # Subtitle
        subtitle = self._subtitle_font.render(
            "Stop Ralph's bricks and repair the windows!",
            True,
            S.WHITE
        )

        screen.blit(
            subtitle,
            subtitle.get_rect(center=(cx, 275))
        )
        
        # draw menu buttons

        self._draw_button(
            screen,
            self._start_button,
            "START GAME",
            "start"
        )

        self._draw_button(
            screen,
            self._quit_button,
            "QUIT",
            "quit"
        )
        
        # draw instructions
        
        instructions = [
            "Arrow keys / WASD : Move    SPACE : Fix a window",
            f"Repair every broken window within {int(S.GAME_DURATION)} seconds!",
            f"You have {S.MAX_LIVES} lives - each brick hit costs one.",
            "Bricks fall faster as time passes!"
        ]

        for i, line in enumerate(instructions):

            text = self._instruction_font.render(
                line,
                True,
                (225, 225, 235)
            )

            screen.blit(
                text,
                text.get_rect(
                    center=(cx, 560 + i * 30)
                )
            )
            
    # buttons
    def _draw_button(self, screen, rect, text, button_name):
        """Draw a button with a hover effect."""

        # Change button colour when the mouse hovers over it.
        if self._hovered_button == button_name:
            button_colour = (255, 190, 50)
        else:
            button_colour = (220, 150, 40)

        # Button background
        pygame.draw.rect(
            screen,
            button_colour,
            rect,
            border_radius=10
        )

        # Button outline
        pygame.draw.rect(
            screen,
            S.WHITE,
            rect,
            width=3,
            border_radius=10
        )

        # Button text
        button_text = self._button_font.render(
            text,
            True,
            S.BLACK
        )

        screen.blit(
            button_text,
            button_text.get_rect(center=rect.center)
        )
        
    def exit(self):
        pass
    
    # structure :
    # enter() --> Preparing the menu as it enters the menu screen
    # draw(screen) --> display everything (menu graphics all here)
    # *** get_rect() creates a rectangle matching image dimensions
    # *** self._draw_button() > Helper method to avoid writing the same drawing code twice - same method can draw both start and quit buttons
    # handle_events(events) --> handles user interaction
    # *** collidepoint() checks whether the mouse click position is inside the button rectangle
    # *** order inside draw() --> Background, Overlay, Titles, Buttons, Instructions
    
