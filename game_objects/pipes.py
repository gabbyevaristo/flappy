import pygame
from creation import image_loader
import constants


PIPE_FILE = 'pipe-green.png'


class BottomPipe:

    def __init__(self, height):
        self.pipe_bottom = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe_bottom = pygame.transform.scale(self.pipe_bottom, (self.pipe_bottom.get_width() + 20, self.pipe_bottom.get_height() * 2))
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(midtop=(constants.SCREEN_WIDTH + self.pipe_bottom.get_width(), height))
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

    def __init__(self, height):
        self.pipe_top = image_loader.ImageLoader.load_image(PIPE_FILE)
        self.pipe_top = pygame.transform.scale(self.pipe_top, (self.pipe_top.get_width() + 20, self.pipe_top.get_height() * 2))
        self.pipe_top = pygame.transform.rotate(self.pipe_top, 180)
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
