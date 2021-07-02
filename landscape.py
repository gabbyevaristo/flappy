import pygame
import image_loader


BACKGROUND_FILE = 'background-night.png'
FLOOR_FILE = 'base.png'

class Landscape:

    def __init__(self):
        self.background = image_loader.ImageLoader.load_image(BACKGROUND_FILE)
        self.background = pygame.transform.scale(self.background, (530, 750))
        self.foreground = image_loader.ImageLoader.load_image(FLOOR_FILE)
        self.foreground = pygame.transform.scale(self.foreground, (530, self.foreground.get_height()))
        self.foreground_x = 0

    def move_foreground(self, speed):
        self.foreground_x -= speed

        if self.foreground_x < self.get_foreground_width() * -1:  # If the bg is at the -width, then reset its position
            self.foreground_x = 0

    def get_foreground_width(self):
        return self.foreground.get_width()

    def get_background(self):
        return self.background

    def get_foreground(self):
        return self.foreground

    def get_foreground_x(self):
        return self.foreground_x

    def set_foreground_x(self, x):
        self.self.foreground_x = x
