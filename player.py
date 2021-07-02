import pygame
from spritesheet import SpriteSheet
import image_loader
from pygame.locals import RLEACCEL


PLAYER_FILE = 'redbird-midflap.png'

class Player():

    def __init__(self, jump_velocity):
        self.player = image_loader.ImageLoader.load_image(PLAYER_FILE)
        self.player = pygame.transform.scale(self.player, (self.player.get_width() + 10, self.player.get_height() + 5))
        self.player_rect = self.player.get_rect(center=(180,355))
        self.jump_velocity = jump_velocity
        self.y = 0

    def get_player_surface(self):
        return self.player

    def get_player_rect(self):
        return self.player_rect

    def move_player(self, gravity):
        self.y += gravity
        self.player_rect.centery += self.y
        if self.player_rect.top <= 0:
            self.player_rect.top = 0
            self.y += 1


    def on_tap(self):
        self.y = 0
        self.y -= self.jump_velocity

    def fall(self):
        self.player_rect.centery += 5

    def reset_player(self):
        self.player_rect.center = (180,355)
