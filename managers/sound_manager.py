"""Centralized sound effects and music manager."""

import pygame


class SoundManager:
    def __init__(self):
        self._sounds = {}
        self._music_volume = 1.0
        self._sound_volume = 1.0

    def load_sounds(self):
        pass

    def play_sound(self, name):
        pass

    def play_music(self, name):
        pass

    def stop_music(self):
        pass

    def set_volume(self, volume):
        pass
