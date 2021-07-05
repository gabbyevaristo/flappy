import pygame
from . import bird_color
from creation import image_loader


RED_DOWNFLAP_FILE = 'redbird-downflap.png'
RED_MIDFLAP_FILE = 'redbird-midflap.png'
RED_UPFLAP_FILE = 'redbird-upflap.png'
BLUE_DOWNFLAP_FILE = 'bluebird-downflap.png'
BLUE_MIDFLAP_FILE = 'bluebird-midflap.png'
BLUE_UPFLAP_FILE = 'bluebird-upflap.png'


class Bird:

    def __init__(self, color):
        if color == bird_color.BirdColor.RED:
            self.downflap = image_loader.ImageLoader.load_image(RED_DOWNFLAP_FILE)
            self.midflap = image_loader.ImageLoader.load_image(RED_MIDFLAP_FILE)
            self.upflap = image_loader.ImageLoader.load_image(RED_UPFLAP_FILE)
        elif color == bird_color.BirdColor.BLUE:
            self.downflap = image_loader.ImageLoader.load_image(BLUE_DOWNFLAP_FILE)
            self.midflap = image_loader.ImageLoader.load_image(BLUE_MIDFLAP_FILE)
            self.upflap = image_loader.ImageLoader.load_image(BLUE_UPFLAP_FILE)
        self.downflap = pygame.transform.scale(
            self.downflap,
            (self.downflap.get_width() + 10, self.downflap.get_height() + 5))
        self.midflap = pygame.transform.scale(
            self.midflap,
            (self.midflap.get_width() + 10, self.midflap.get_height() + 5))
        self.upflap = pygame.transform.scale(
            self.upflap,
            (self.upflap.get_width() + 10, self.upflap.get_height() + 5))
        self.bird_frames = [self.downflap, self.midflap, self.upflap]
        self.bird_index = 0
        self.initial_pos = (180,355)
        self.bird = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird.get_rect(center=self.initial_pos)
        self.y = 0


    def draw_bird(self, screen):
        screen.blit(self.rotate_bird(), self.bird_rect)


    def move_bird(self, gravity):
        self.y += gravity
        self.bird_rect.centery += self.y

        # Let bird fall if it hits the top of the screen
        if self.bird_rect.top <= 0:
            self.bird_rect.top = 0
            self.y += 1


    def on_tap(self, jump_velocity):
        self.y = 0
        self.y -= jump_velocity


    def fall(self, floor_height, fall_rate):
        if self.bird_rect.bottom <= floor_height:
            self.bird_rect.centery += fall_rate


    def rotate_bird(self):
        return pygame.transform.rotozoom(self.bird, -self.y * 3, 1)


    def change_bird_frame(self):
        if self.bird_index < len(self.bird_frames) - 1:
            self.bird_index += 1
        else:
            self.bird_index = 0

        self.bird = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird.get_rect(
            center=(self.initial_pos[0], self.bird_rect.centery))


    def reset_bird(self):
        self.bird_rect.center = self.initial_pos
        self.y = 0


    def get_bird_rect(self):
        return self.bird_rect
