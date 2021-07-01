import pygame
import image_loader
import constants
import json


class SpriteSheet:

    def __init__(self, filename, sheet_length):
        self.filename = filename
        self.sprite_sheet = image_loader.ImageLoader.load_image(f'{filename}.png')
        self.sheet_length = sheet_length
        self.json_file = f'{filename}.json'
        with open(self.json_file) as f:
            self.data = json.load(f)
        self.sprites = self.create_sprites()

    def create_sprites(self):
        sprites = []
        for i in range(1, self.sheet_length + 1):
            filename = f'{self.filename}_{i}.png'
            sprite = self.create_sprite(filename, i)
            sprites.append(sprite)
        return sprites

    def create_sprite(self, filename, i):
        sprite = self.data[filename]['frame']
        x, y, width, height = sprite['x'], sprite['y'], sprite['w'], sprite['h']

        surface = pygame.Surface((width, height))
        surface.set_colorkey(constants.BLACK)

        # blitting sprite from sprite_sheet
        surface.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return surface

    def get_sprites(self):
        return self.sprites
