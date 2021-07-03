import pygame
import pipes
import random


class PipeManager:

    def __init__(self):
        self.pipes = []
        self.pipe_heights = [x for x in range(250,600,10)]

    def get_pipes(self):
        return self.pipes

    def move_pipes(self, speed):
        for pipe in self.pipes:
            pipe_rect = pipe.get_pipe_rect()
            pipe_rect.centerx -= speed

    def add_pipe(self):
        height = random.choice(self.pipe_heights)
        bottom_pipe = pipes.BottomPipe(height)
        top_pipe = pipes.TopPipe(height - 200)
        self.pipes.append(bottom_pipe)
        self.pipes.append(top_pipe)

    def clear_pipes(self):
        self.pipes.clear()