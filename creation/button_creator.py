import pygame
import constants
from . import text_creator
import os


class ButtonCreator:

    def __init__(self, x, y, width, height, size, text, color_text, color_fill):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # For buttons, text will not actually be placed at position (0,0)
        self.text = text_creator.TextCreator(
            position=(0,0), size=size, text=text, color=color_text)
        self.color_fill = color_fill


    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color_fill,
            (self.x, self.y, self.width, self.height), 0)
        text = self.text.get_text_surface()
        x = self.x + (self.width // 2 - text.get_width() // 2)
        y = self.y + (self.height // 2 - text.get_height() // 2)
        screen.blit(text, (x, y))


    def change_color_fill(self, color):
        self.color_fill = color


    def is_mouse_over(self, position):
        x, y = position
        if (self.x < x < self.x + self.width and
            self.y < y < self.y + self.height):
            return True
        return False
