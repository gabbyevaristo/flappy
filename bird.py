import pygame
import image_loader


RED_DOWNFLAP_FILE = 'redbird-downflap.png'
RED_MIDFLAP_FILE = 'redbird-midflap.png'
RED_UPFLAP_FILE = 'redbird-upflap.png'


class Bird:

    def __init__(self, jump_velocity):
        self.bird_downflap = image_loader.ImageLoader.load_image(RED_DOWNFLAP_FILE)
        self.bird_downflap = pygame.transform.scale(self.bird_downflap, (self.bird_downflap.get_width() + 10, self.bird_downflap.get_height() + 5))
        self.bird_midflap = image_loader.ImageLoader.load_image(RED_MIDFLAP_FILE)
        self.bird_midflap = pygame.transform.scale(self.bird_midflap, (self.bird_midflap.get_width() + 10, self.bird_midflap.get_height() + 5))
        self.bird_upflap = image_loader.ImageLoader.load_image(RED_UPFLAP_FILE)
        self.bird_upflap = pygame.transform.scale(self.bird_upflap, (self.bird_upflap.get_width() + 10, self.bird_upflap.get_height() + 5))
        self.bird_frames = [self.bird_downflap, self.bird_midflap, self.bird_upflap]
        self.bird_index = 0
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(180,355))
        self.jump_velocity = jump_velocity
        self.y = 0

    def get_bird_surface(self):
        return self.bird_surface

    def get_bird_rect(self):
        return self.bird_rect

    def move_bird(self, gravity):
        self.y += gravity
        self.bird_rect.centery += self.y
        if self.bird_rect.top <= 0:
            self.bird_rect.top = 0
            self.y += 1

    def on_tap(self):
        self.y = 0
        self.y -= self.jump_velocity

    def fall(self):
        self.bird_rect.centery += 5

    def reset_bird(self):
        self.bird_rect.center = (180,355)
        self.y = 0

    def rotate_bird(self):
        return pygame.transform.rotozoom(self.bird_surface, -self.y * 3, 1)

    def change_bird_frame(self):
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0

        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(180, self.bird_rect.centery))