import pygame
import image_loader


class Logo:

    def __init__(self):
        self.logo = image_loader.ImageLoader.load_image('logo.png')
        self.logo = pygame.transform.scale(self.logo, (385,135))

    def draw_logo(self, screen):
        screen.blit(self.logo, (60,150))
