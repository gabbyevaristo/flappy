import pygame


class Screen:

    def __init__(self, width, height, name='Flappy Bird'):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

    def update_screen(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen
