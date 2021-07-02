import pygame
import constants
import os

FONT_DIR = 'fonts'

class Text:

    def __init__(self, size, text, color, position):
        self.font = pygame.font.Font(os.path.join(FONT_DIR, constants.FONT_FILE), size)
        self.font_surface = self.font.render(text, True, color)
        self.font_rect = self.font_surface.get_rect(center=position)
        self.color = color

    def change_text(self, text):
        self.font_surface = self.font.render(text, True, self.color)

    def get_font_surface(self):
        return self.font_surface

    def get_font_rect(self):
        return self.font_rect
