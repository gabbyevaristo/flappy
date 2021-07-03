import pygame
import constants
import screen
import landscape
import sys
import single_player
import game_assets

pygame.init()


class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = screen.Screen(self.width, self.height)
        self.landscape = landscape.Landscape()
        self.logo = game_assets.Logo()
        self.mode = None

    def run_game(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            self.check_events()

            if self.mode == 'SINGLE':
                single_player.SinglePlayer(self.screen, self.landscape, clock)
                self.clear_mode()

            self.draw_objects()
            self.screen.update_screen()

            clock.tick(constants.FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.mode = 'SINGLE'

    def draw_objects(self):
        screen = self.screen.get_screen()

        self.landscape.draw_background(screen)
        self.landscape.draw_foreground(screen)
        self.logo.draw_logo(screen)

    def clear_mode(self):
        self.mode = None
