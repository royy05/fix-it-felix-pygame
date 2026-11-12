"""Abstract base class for all game screens/states."""

from abc import ABC, abstractmethod


class GameState(ABC):
    def __init__(self, game_manager):
        self._game_manager = game_manager

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def exit(self):
        pass
