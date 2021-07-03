import pygame
import image_loader
import constants


class StartText:

    def __init__(self):
        self.start = image_loader.ImageLoader.load_image('press-to-start.png')
        self.start = pygame.transform.scale(self.start, (385,95))
        self.start_rect = self.start.get_rect(center=(constants.SCREEN_WIDTH // 2, 150))

    def draw_start(self, screen):
        screen.blit(self.start, self.start_rect)



class GameOverText:

    def __init__(self):
        self.game_over = image_loader.ImageLoader.load_image('gameover.png')
        self.game_over = pygame.transform.scale(self.game_over, (360,80))
        self.game_over_rect = self.game_over.get_rect(center=(constants.SCREEN_WIDTH // 2, 190))

    def draw_game_over(self, screen):
        screen.blit(self.game_over, self.game_over_rect)
