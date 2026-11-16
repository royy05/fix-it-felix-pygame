"""Game-over screen."""

import pygame

from states.game_state import GameState




class LoseState(GameState):
    def enter(self):
        self._title_font = pygame.font.Font(None,72)
        self._instruction_font = pygame.font.Font(None,30)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from states.menu_state import MenuState
                    self._game_manager.change_state(
                        MenuState(self._game_manager)
                    )
                elif event.key == pygame.K_SPACE:
                    from states.playing_state import PlayingState
                    self._game_manager.change_state(
                        PlayingState(self._game_manager)
                    )

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((20,22,32))
        pygame.draw.rect(
            screen,
            (230,60,60),
            (30,30,740,660),
            4
        )
        title = self._title_font.render(
            "GAME OVER",
            True,
            (230,60,60)
        )
        title_rect = title.get_rect(center=(400, 360))
        screen.blit(title,title_rect)

        menu_text = self._instruction_font.render(
            "Press ENTER to return to Menu",
            True,
            (255,255,255)
        )
        restart_text = self._instruction_font.render(
            "Press SPACE to Play Again",
            True,
            (255,255,255)
        )

        menu_rect = menu_text.get_rect(center=(400,430))
        restart_rect = restart_text.get_rect(center=(400,475))
        screen.blit(menu_text,menu_rect)
        screen.blit(restart_text,restart_rect)


    def exit(self):
        pass
