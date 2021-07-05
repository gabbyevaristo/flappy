import pygame
import constants
import os


FONT_DIR = 'fonts'
ARCADE_FONT = 'arcade-font.ttf'


class TextCreator:

    def __init__(self, position, size, text, color):
        try:
            font_name = os.path.join(FONT_DIR, ARCADE_FONT)
            font = pygame.font.Font(font_name, size)
        except FileNotFoundError:
            print("[ERROR] Cannot find font file: " + font_name)
            raise SystemExit()
        except pygame.error as e:
            raise SystemExit(e)
        else:
            self.font = font
            self.text = self.font.render(text, True, color)
            self.text_rect = self.text.get_rect(center=position)
            self.position = position
            self.color = color


    def update_text(self, text, color=None):
        if not color:
            color = self.color
        self.text = self.font.render(str(text), True, color)
        self.text_rect = self.text.get_rect(center=self.position)


    def get_text_surface(self):
        return self.text


    def get_text_rect(self):
        return self.text_rect
