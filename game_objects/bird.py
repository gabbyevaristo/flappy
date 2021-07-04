import pygame
import constants
from creation import image_loader


RED_DOWNFLAP_FILE = 'redbird-downflap.png'
RED_MIDFLAP_FILE = 'redbird-midflap.png'
RED_UPFLAP_FILE = 'redbird-upflap.png'
FALL_RATE = 4

class Bird:

    def __init__(self):
        self.bird_downflap = image_loader.ImageLoader.load_image(RED_DOWNFLAP_FILE)
        self.bird_downflap = pygame.transform.scale(self.bird_downflap, (self.bird_downflap.get_width() + 10, self.bird_downflap.get_height() + 5))
        self.bird_midflap = image_loader.ImageLoader.load_image(RED_MIDFLAP_FILE)
        self.bird_midflap = pygame.transform.scale(self.bird_midflap, (self.bird_midflap.get_width() + 10, self.bird_midflap.get_height() + 5))
        self.bird_upflap = image_loader.ImageLoader.load_image(RED_UPFLAP_FILE)
        self.bird_upflap = pygame.transform.scale(self.bird_upflap, (self.bird_upflap.get_width() + 10, self.bird_upflap.get_height() + 5))
        self.bird_frames = [self.bird_downflap, self.bird_midflap, self.bird_upflap]
        self.bird_index = 0
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_center = (180,355)
        self.bird_rect = self.bird_surface.get_rect(center=self.bird_center)
        self.y = 0

    def get_bird_rect(self):
        return self.bird_rect

    def move_bird(self):
        self.y += constants.GRAVITY
        self.bird_rect.centery += self.y
        if self.bird_rect.top <= 0:
            self.bird_rect.top = 0
            self.y += 1

    def on_tap(self):
        self.y = 0
        self.y -= constants.JUMP_VELOCITY

    def fall(self):
        if self.bird_rect.bottom < constants.FLOOR_HEIGHT:
            self.bird_rect.centery += FALL_RATE

    def reset_bird(self):
        self.bird_rect.center = self.bird_center
        self.y = 0

    def rotate_bird(self):
        return pygame.transform.rotozoom(self.bird_surface, -self.y * 3, 1)

    def change_bird_frame(self):
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0

        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(self.bird_center[0], self.bird_rect.centery))

    def draw_bird(self, screen):
        screen.blit(self.rotate_bird(), self.bird_rect)
