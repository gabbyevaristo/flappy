import pygame
from . import pipes
from creation import image_loader
import constants
import random


PIPE_FILE = 'pipe-green.png'


class PipeManager:

    def __init__(self):
        self.pipe = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe = pygame.transform.scale(self.pipe, (self.pipe.get_width() + 20, self.pipe.get_height() * 2))
        self.pipes = []
        self.pipe_heights = [i for i in range(250,600,10)]

    def get_pipes(self):
        return self.pipes

    def get_individual_pipes(self):
        pipes = []
        for pipe_bottom, pipe_top in self.pipes:
            pipes.append(pipe_bottom)
            pipes.append(pipe_top)
        return pipes

    def move_pipes(self, speed):
        for pipe in self.get_individual_pipes():
            pipe_rect = pipe.get_pipe_rect()
            pipe_rect.centerx -= speed

    def add_pipe(self):
        height = random.choice(self.pipe_heights)
        bottom_pipe = pipes.BottomPipe(self.pipe, height)
        top_pipe = pipes.TopPipe(self.pipe, height - constants.PIPE_GAP)
        self.pipes.append((bottom_pipe, top_pipe))

    def clear_pipes(self):
        self.pipes.clear()

    def draw_pipes(self, screen):
        for pipe in self.get_individual_pipes():
            pipe_surface, pipe_rect = pipe.get_pipe_surface(), pipe.get_pipe_rect()
            screen.blit(pipe_surface, pipe_rect)
