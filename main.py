"""Application entry point for Fix-It Felix Jr."""

import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS
from managers.game_manager import GameManager


def main():
    """Initialize Pygame and start the game manager."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    game_manager = GameManager(screen)
    game_manager.run()

    pygame.quit()


if __name__ == "__main__":
    main()
