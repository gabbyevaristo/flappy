import pygame
import game_assets
import constants
from game_objects import screen, landscape
from single_player import single_player_mode
from game_modes import GameModes
import sys


pygame.init()


class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = screen.Screen(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.landscape = landscape.Landscape(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
            constants.FLOOR_HEIGHT)
        self.logo = game_assets.Logo(constants.SCREEN_WIDTH)
        self.one_player_button = game_assets.OnePlayerButton()
        self.multi_player_button = game_assets.MultiPlayerButton()
        self.mode = None
        self.clock = None


    def run_game(self):
        self.clock = pygame.time.Clock()

        run = True
        while run:
            self.check_events()
            self.check_mode()
            self.draw_objects()
            self.screen.update_screen()
            self.clock.tick(constants.FPS)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_position = pygame.mouse.get_pos()

            # Fill button with specified color when button is hovered
            if event.type == pygame.MOUSEMOTION:
                self.one_player_button.fill_one_player_button(mouse_position)
                self.multi_player_button.fill_multi_player_button(mouse_position)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.one_player_button.is_mouse_over(mouse_position):
                    self.mode = GameModes.SINGLE
                elif self.multi_player_button.is_mouse_over(mouse_position):
                    self.mode = GameModes.MULTI


    def check_mode(self):
        # Instantiate single or multi player mode
        if self.mode == GameModes.SINGLE:
            single_player_mode.SinglePlayerMode(
                self.screen, self.clock, self.landscape)
            self.clear_mode()
        elif self.mode == GameModes.MULTI:
            pass


    def draw_objects(self):
        screen = self.screen.get_screen()
        self.landscape.draw_background(screen)
        self.landscape.draw_foreground(screen)
        self.logo.draw_logo(screen)
        self.one_player_button.draw_one_player_button(screen)
        self.multi_player_button.draw_multi_player_button(screen)


    def clear_mode(self):
        self.mode = None
