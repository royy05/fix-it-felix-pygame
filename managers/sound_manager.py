"""Centralized sound effects and music manager."""

import pygame
from events import (
    PLAYER_DAMAGED,
    WINDOW_REPAIRED,
    GAME_WON,
    GAME_LOST,
    RALPH_DESTROYED_WINDOW,
    RALPH_ATTACKED

)


class SoundManager:
    def __init__(self):
        
        self._sounds = {}
        self._music_volume = 1.0
        self._sound_volume = 1.0

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.load_sounds()
        self.set_volume(1.0)

    def handle_event(self,event):
        if event.type == PLAYER_DAMAGED:
            self.play_sound("damage")

        elif event.type == WINDOW_REPAIRED:
            self.play_sound('hammer')

        elif event.type == GAME_WON:
            self.play_sound("victory")

        elif event.type == GAME_LOST:
            self.play_sound("game_over")

        elif event.type == RALPH_DESTROYED_WINDOW:
            self.play_sound("ralph_smash")

        elif event.type == RALPH_ATTACKED:
            self.play_sound("ralph_attack")


    def load_sounds(self):
        self._sounds = {
            "game_over": pygame.mixer.Sound("assets/audio/lose.wav"),
            "damage": pygame.mixer.Sound("assets/audio/felixgetsdamage.wav"),
            "hammer": pygame.mixer.Sound("assets/audio/felixrepair.wav"),
            "ralph_smash": pygame.mixer.Sound("assets/audio/ralphdestorywindow.wav"),
            "ralph_attack": pygame.mixer.Sound("assets/audio/ralphdestory.wav"),
            "victory": pygame.mixer.Sound("assets/audio/win.wav")
        }

    def play_sound(self, name):
        if name in self._sounds:
            self._sounds[name].play()

        else:
            print(f"Sound '{name}' not found.")

    def play_music(self, name):
        if name == "background":
            if not pygame.mixer.music.get_busy():

                pygame.mixer.music.load("assets/audio/backgroundsound.mp4")
                pygame.mixer.music.set_volume(self._music_volume)
                pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        if volume < 0 or volume > 1:
            raise ValueError("Volume must be between 0 and 1")

        self._sound_volume = volume
        self._music_volume = volume

        for sound in self._sounds.values():
            sound.set_volume(self._sound_volume)

        pygame.mixer.music.set_volume(self._music_volume)
