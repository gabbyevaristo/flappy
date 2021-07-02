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
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def draw(self, obj, pos):
        self.screen.blit(obj, pos)
