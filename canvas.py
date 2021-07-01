import pygame
import os

"""
Responsible for the screen and drawing

"""
class Canvas:

    def __init__(self, width, height, name='Flappy'):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

    def update_screen(self):
        pygame.display.update()

    def get_screen(self):
        return self.screen

    def draw_background(self, background, x1, x2):
        self.screen.blit(background, (x1, 0))
        self.screen.blit(background, (x2, 0))

    def draw(self, obj, pos):
        self.screen.blit(obj, pos)
