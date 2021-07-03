import pygame
import text_creator
import constants
import os


FONT_DIR = 'fonts'


class ButtonCreator:

    def __init__(self, x, y, width, height, text, color_text, color_fill, size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color_text = color_text
        self.color_fill = color_fill
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_fill, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.Font(os.path.join(FONT_DIR, constants.FONT_FILE), self.size)
        text = font.render(self.text, 1, self.color_text)
        screen.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def change_color_fill(self, color):
        self.color_fill = color

    def is_mouse_over(self, position):
        x, y = position
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        return False
