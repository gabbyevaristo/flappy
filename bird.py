import pygame
import image_loader


RED_DOWNFLAP_FILE = 'redbird-downflap.png'
RED_MIDFLAP_FILE = 'redbird-midflap.png'
RED_UPFLAP_FILE = 'redbird-upflap.png'


class Bird:

    def __init__(self, jump_velocity):
        self.bird = image_loader.ImageLoader.load_image(RED_MIDFLAP_FILE)
        self.bird = pygame.transform.scale(self.bird, (self.bird.get_width() + 10, self.bird.get_height() + 5))
        self.bird_rect = self.bird.get_rect(center=(180,355))
        self.jump_velocity = jump_velocity
        self.y = 0

    def get_bird_surface(self):
        return self.bird

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
        return pygame.transform.rotozoom(self.bird, -self.y * 3, 1)
