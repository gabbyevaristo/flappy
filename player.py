import pygame
# from spritesheet import SpriteSheet, Sprite
from spritesheet import SpriteSheet
import image_loader
from pygame.locals import RLEACCEL


PLAYER_FILE = 'astronauts_sheet'

class Player():

    def __init__(self):
        self.sprite_sheet = SpriteSheet(PLAYER_FILE)
        self.sprite_files = [f'astronaut{i}.png' for i in range(1,10)]
        self.player_sprites = list(map(self.sprite_sheet.parse_sprite, self.sprite_files))

    def get_player_sprites(self):
        return self.player_sprites
