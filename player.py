import pygame
# from spritesheet import SpriteSheet, Sprite
from spritesheet import SpriteSheet
import image_loader
from pygame.locals import RLEACCEL


PLAYER_FILE = 'astronauts_sheet'
PLAYER_LEN = 9

class Player():

    def __init__(self):
        self.player_sheet = SpriteSheet(PLAYER_FILE, PLAYER_LEN)
        self.player_sprites = self.player_sheet.get_sprites()

    def get_player_sprites(self):
        return self.player_sprites
