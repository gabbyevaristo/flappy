import pygame
import constants
import canvas
import landscape
import os
import sys
import single_player
import image_loader

pygame.init()



class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = canvas.Canvas(self.width, self.height)
        self.landscape = landscape.Landscape()
        self.game_speed = constants.INIT_GAME_SPEED
        self.mode = None
        self.logo = image_loader.ImageLoader.load_image('logo.png')
        self.logo = pygame.transform.scale(self.logo, (385,135))

    def run_game(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            self.check_events()
            if self.mode == 'single':
                g = single_player.SinglePlayer(self.screen, self.landscape, clock)
                self.mode = None
            self.draw_objects()
            self.screen.update_screen()

            clock.tick(constants.FPS)

    def draw_objects(self):
        # Background
        background = self.landscape.get_background()
        self.screen.draw(background, (0, 0))

        # Foreground
        foreground, foreground_x = self.landscape.get_foreground(), self.landscape.get_foreground_x()
        self.screen.draw(foreground, (foreground_x, constants.FLOOR_HEIGHT))
        self.screen.draw(foreground, (foreground_x + self.landscape.get_foreground_width(), constants.FLOOR_HEIGHT))

        self.screen.draw(self.logo, (60,150))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.mode = 'single'
