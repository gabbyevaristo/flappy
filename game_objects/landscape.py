import pygame
from creation import image_loader


DAY_BG_FILE = 'background-day.png'
NIGHT_BG_FILE = 'background-night.png'
FLOOR_FILE = 'floor.png'


class Landscape:

    def __init__(self, screen_width, screen_height, floor_height):
        self.background = image_loader.ImageLoader.load_image(DAY_BG_FILE)
        self.background = pygame.transform.scale(
            self.background, (screen_width, screen_height))
        self.foreground = image_loader.ImageLoader.load_image(FLOOR_FILE)
        self.foreground = pygame.transform.scale(
            self.foreground, (screen_width, self.foreground.get_height()))
        self.foreground_x = 0
        self.floor_height = floor_height


    def draw_background(self, screen):
        screen.blit(self.background, (0,0))


    def draw_foreground(self, screen):
        screen.blit(self.foreground, (self.foreground_x, self.floor_height))
        foreground_x_2 = self.foreground_x + self.get_foreground_width()
        screen.blit(self.foreground, (foreground_x_2, self.floor_height))


    def move_foreground(self, speed):
        self.foreground_x -= speed

        # If the foreground is at the -width, then reset its position
        if self.foreground_x < self.get_foreground_width() * -1:
            self.foreground_x = 0


    def get_foreground_width(self):
        return self.foreground.get_width()
