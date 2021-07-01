import pygame
import image_loader
import constants
import json


class SpriteSheet:

    def __init__(self, filename):
        self.sprite_sheet = image_loader.ImageLoader.load_image(f'{filename}.png')
        self.json_file = f'{filename}.json'
        with open(self.json_file) as f:
            self.data = json.load(f)

    def parse_sprite(self, filename):
        sprite = self.data[filename]['frame']
        x, y, width, height = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x, y, width, height)
        return image

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))    # empty surface for image
        sprite.set_colorkey(constants.BLACK)
        sprite.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return sprite
