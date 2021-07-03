import pygame
import image_loader
import constants


BACKGROUND_FILE = 'background-day.png'
FLOOR_FILE = 'base.png'

class Landscape:

    def __init__(self):
        self.background = image_loader.ImageLoader.load_image(BACKGROUND_FILE)
        self.background = pygame.transform.scale(self.background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.foreground = image_loader.ImageLoader.load_image(FLOOR_FILE)
        self.foreground = pygame.transform.scale(self.foreground, (constants.SCREEN_WIDTH, self.foreground.get_height()))
        self.foreground_x = 0

    def move_foreground(self, speed):
        self.foreground_x -= speed

        if self.foreground_x < self.get_foreground_width() * -1:  # If the bg is at the -width, then reset its position
            self.foreground_x = 0

    def get_foreground_width(self):
        return self.foreground.get_width()

    def draw_background(self, screen):
        screen.blit(self.background, (0,0))

    def draw_foreground(self, screen):
        screen.blit(self.foreground, (self.foreground_x, constants.FLOOR_HEIGHT))
        screen.blit(self.foreground, (self.foreground_x + self.foreground.get_width(), constants.FLOOR_HEIGHT))
