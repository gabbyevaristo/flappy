import pygame
import os


IMG_DIR = 'images'


class ImageLoader:

    @staticmethod
    def load_image(filename):
        try:
            image_name = os.path.join(IMG_DIR, filename)
            image = pygame.image.load(image_name)
        except FileNotFoundError:
            print("[ERROR] Cannot find image file: " + image_name)
            raise SystemExit()
        except pygame.error as e:
            raise SystemExit(e)
        else:
            return image.convert_alpha()
