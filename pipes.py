import pygame
import image_loader
import constants
import random


PIPE_FILE = 'pipe-green.png'

class TopPipe:

    def __init__(self, height):
        self.pipe_top = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe_top = pygame.transform.scale(self.pipe_top, (self.pipe_top.get_width() + 20, self.pipe_top.get_height() * 2))
        self.pipe_top = pygame.transform.rotate(self.pipe_top, 180)
        self.pipe_top_rect = self.pipe_top.get_rect(midbottom=(550, height))
        self.has_passed = False

    def get_pipe_surface(self):
        return self.pipe_top

    def get_pipe_rect(self):
        return self.pipe_top_rect

    def is_pipe_passed(self):
        return self.has_passed

    def set_pass_true(self):
        self.has_passed = True


class BottomPipe:

    def __init__(self, height):
        self.pipe_bottom = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe_bottom = pygame.transform.scale(self.pipe_bottom, (self.pipe_bottom.get_width() + 20, self.pipe_bottom.get_height() * 2))
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(midtop=(550, height))
        self.has_passed = False

    def get_pipe_surface(self):
        return self.pipe_bottom

    def get_pipe_rect(self):
        return self.pipe_bottom_rect

    def is_pipe_passed(self):
        return self.has_passed

    def set_pass_true(self):
        self.has_passed = True
