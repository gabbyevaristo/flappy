import pygame
import os


IMG_DIR = 'images'

class ImageLoader:

    @staticmethod
    def load_image(file_name=''):
        return pygame.image.load(os.path.join(IMG_DIR, file_name)).convert_alpha()
