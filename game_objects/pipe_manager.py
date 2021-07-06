import pygame
from . import pipes
from creation import image_loader
import game_modes
import random


GREEN_PIPE_FILE = 'pipe-green.png'
RED_PIPE_FILE = 'pipe-red.png'


class PipeManager:

    def __init__(self, mode):
        self.mode = mode
        self.pipe = image_loader.ImageLoader.load_image(GREEN_PIPE_FILE)
        self.pipe = pygame.transform.scale(
            self.pipe, (self.pipe.get_width() + 20, self.pipe.get_height() * 2))
        self.pipes = []
        self.pipe_heights_single = [i for i in range(250,600,10)]
        self.pipe_heights_multi = [400,410,240,350,550,270,300,340,390,570,450]
        self.height_index = 0


    def draw_pipes(self, screen):
        for pipe in self.get_individual_pipes():
            pipe_surface = pipe.get_pipe_surface()
            pipe_rect = pipe.get_pipe_rect()
            screen.blit(pipe_surface, pipe_rect)


    def move_pipes(self, speed):
        for pipe in self.get_individual_pipes():
            pipe_rect = pipe.get_pipe_rect()
            pipe_rect.centerx -= speed


    def add_pipe(self, screen_width, pipe_gap):
        if self.mode == game_modes.GameModes.SINGLE:
            height = random.choice(self.pipe_heights_single)
        else:
            if self.height_index < len(self.pipe_heights_multi) - 1:
                self.height_index += 1
            else:
                self.height_index = 0
            height = self.pipe_heights_multi[self.height_index]

        bottom_pipe = pipes.BottomPipe(
            pipe=self.pipe, screen_width=screen_width, height=height)
        top_pipe = pipes.TopPipe(
            pipe=self.pipe, screen_width=screen_width, height=height - pipe_gap)
        self.pipes.append((bottom_pipe, top_pipe))


    def clear_pipes(self):
        self.height_index = 0
        self.pipes.clear()


    def get_individual_pipes(self):
        return [pipe for pipes in self.pipes for pipe in pipes]


    def get_pipes(self):
        return self.pipes
