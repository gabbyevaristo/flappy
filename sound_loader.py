import pygame
import sound_names
import os


SOUND_DIR = 'sounds'

class SoundLoader:

    def __init__(self):
        self.flap_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'flap.wav'))
        self.collide_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'collide.wav'))
        self.point_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'point.wav'))
        self.sounds = {}
        self.create_sound_map()

    def create_sound_map(self):
        self.sounds[sound_names.SoundNames.FLAP] = self.flap_sound
        self.sounds[sound_names.SoundNames.COLLIDE] = self.collide_sound
        self.sounds[sound_names.SoundNames.POINT] = self.point_sound

    def play_sound(self, sound):
        self.sounds[sound].play()
