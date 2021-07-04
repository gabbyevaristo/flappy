import pygame
from creation import image_loader
import constants



class BottomPipe:

    def __init__(self, pipe, height):
        self.pipe_bottom = pipe
        self.pipe_bottom_rect = pipe.get_rect(midtop=(constants.SCREEN_WIDTH + pipe.get_width(), height))
        self.is_passed = False

    def get_pipe_surface(self):
        return self.pipe_bottom

    def get_pipe_rect(self):
        return self.pipe_bottom_rect

    def is_pipe_passed(self):
        return self.is_passed

    def set_passed_true(self):
        self.is_passed = True



class TopPipe:

    def __init__(self, pipe, height):
        self.pipe_top = pygame.transform.rotate(pipe, 180)
        self.pipe_top_rect = self.pipe_top.get_rect(midbottom=(constants.SCREEN_WIDTH + self.pipe_top.get_width(), height))
        self.is_passed = False

    def get_pipe_surface(self):
        return self.pipe_top

    def get_pipe_rect(self):
        return self.pipe_top_rect

    def is_pipe_passed(self):
        return self.is_passed

    def set_passed_true(self):
        self.is_passed = True
