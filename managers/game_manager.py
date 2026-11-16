"""Application loop and game-state coordinator."""

import pygame

from config import FPS, BACKGROUND_COLOR
from states.menu_state import MenuState
from managers.sound_manager import SoundManager

class GameManager:
    def __init__(self, screen):
        
        
        self._screen = screen
        self._clock = pygame.time.Clock()
        self._running = True
        self._sound_manager = SoundManager()
        self._current_state = MenuState(self)
        self._current_state.enter()

    @property
    def current_state(self):
      return self._current_state

    def change_state(self, new_state): #Switches the game from one state to another
        if self._current_state is not None:
            self._current_state.exit()
        self._current_state = new_state
        self._current_state.enter()

    def run(self):
        """Run the main event, update and draw loop."""
        while self._running:
            dt = self._clock.tick(FPS) / 1000.0
            events = pygame.event.get()

            self.handle_events(events)
            if not self._running:
                break
            self.update(dt)
            self.draw()

        self.shutdown()

    def handle_events(self, events): #process user's input and window events
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False
                return

            self._sound_manager.handle_event(event)

            
        if self._current_state is not None:
            self._current_state.handle_events(events)       #forwards all events to the active state; each will do its respective handle_events

    def update(self, dt): #updates game logic and objects
        if self._current_state is not None:
            self._current_state.update(dt)

    def draw(self): #display everything on screen
        self._screen.fill(BACKGROUND_COLOR)
        if self._current_state is not None:
            self._current_state.draw(self._screen)
            
        pygame.display.flip()

    def quit(self):
        """Request the game loop to stop."""
        self._running = False
        
    def shutdown(self):
        """ clean up game resources and shut down pygame """
        if self._current_state is not None:
            self._current_state.exit()
            self._current_state = None
            
        if pygame.mixer.get_init():
            self._sound_manager.stop_music()
        
        pygame.quit()
        
# quit and shutdown structure :
# quit() sets _running = False so the game loop stops
# shutdown() exits the active state
# music is stopped if the mixer is initialized
# pygame.quit() is called once.
        