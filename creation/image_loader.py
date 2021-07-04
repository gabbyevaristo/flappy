import pygame
import os


IMG_DIR = 'images'

class ImageLoader:

    @staticmethod
    def load_image(filename=''):
        print(os.path.join(IMG_DIR, filename))
        return pygame.image.load(os.path.join(IMG_DIR, filename)).convert_alpha()
