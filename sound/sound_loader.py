import pygame
from . import sound_names
import os


SOUND_DIR = 'sounds'


class SoundLoader:

    def __init__(self):
        try:
            flap_sound_file = os.path.join(SOUND_DIR, 'flap.wav')
            flap_sound = pygame.mixer.Sound(flap_sound_file)
            collide_sound_file = os.path.join(SOUND_DIR, 'collide.wav')
            collide_sound = pygame.mixer.Sound(collide_sound_file)
            point_sound_file = os.path.join(SOUND_DIR, 'point.wav')
            point_sound = pygame.mixer.Sound(point_sound_file)
        except FileNotFoundError as e:
            print(f"[ERROR] Cannot load sound. {e}")
            raise SystemExit()
        except pygame.error as e:
            raise SystemExit(e)
        else:
            self.flap_sound = flap_sound
            self.collide_sound = collide_sound
            self.point_sound = point_sound
            self.sounds = {}
            self.create_sound_map()


    def create_sound_map(self):
        self.sounds[sound_names.SoundNames.FLAP] = self.flap_sound
        self.sounds[sound_names.SoundNames.COLLIDE] = self.collide_sound
        self.sounds[sound_names.SoundNames.POINT] = self.point_sound


    def play_sound(self, sound):
        self.sounds[sound].play()
