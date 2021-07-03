import pygame
import constants
import os

FONT_DIR = 'fonts'

class TextCreator:

    def __init__(self, size, text, color, position):
        self.font = pygame.font.Font(os.path.join(FONT_DIR, constants.FONT_FILE), size)
        self.font_surface = self.font.render(text, True, color)
        self.font_rect = self.font_surface.get_rect(center=position)
        self.position = position
        self.color = color

    def update_text(self, text, color=None):
        if not color:
            color = self.color
        self.font_surface = self.font.render(text, True, color)
        self.font_rect =  self.font_surface.get_rect(center=self.position)

    def get_text_surface(self):
        return self.font_surface

    def get_text_rect(self):
        return self.font_rect
