import pygame
import image_loader
import constants
import random


PIPE_FILE = 'pipe-green.png'

class Pipes:

    def __init__(self):
        self.pipe_bottom = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe_bottom = pygame.transform.scale(self.pipe_bottom, (self.pipe_bottom.get_width() + 20, self.pipe_bottom.get_height() * 2))
        self.pipe_top = pygame.transform.rotate(self.pipe_bottom, 180)
        self.pipes = []
        self.pipe_heights = [x for x in range(250,600,10)]

    def get_pipe(self, pipe):
        if pipe.bottom >= 750:
            return self.pipe_bottom
        else:
            return self.pipe_top

    def get_pipes(self):
        return self.pipes

    def add_pipe(self):
        pipe = self.create_pipe()
        self.pipes.extend(pipe)

    def create_pipe(self):
        height = random.choice(self.pipe_heights)
        pipe_bottom = self.pipe_bottom.get_rect(midtop=(550, height))
        pipe_top = self.pipe_top.get_rect(midbottom=(550, height - 150))
        return pipe_bottom, pipe_top

    def move_pipes(self, speed):
        for pipe in self.pipes:
            pipe.centerx -= speed
