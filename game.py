import pygame
import constants
import game_assets
import screen, landscape
import single_player_mode
import sys
from enum import Enum


pygame.init()


class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = screen.Screen(self.width, self.height)
        self.landscape = landscape.Landscape()
        self.logo = game_assets.Logo()
        self.one_player_button = game_assets.OnePlayerButton()
        self.multi_player_button = game_assets.MultiPlayerButton()
        self.mode = None

    def run_game(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            self.check_events()

            if self.mode == GameModes.SINGLE:
                single_player_mode.SinglePlayer(self.screen, self.landscape, clock)
                self.clear_mode()

            self.draw_objects()
            self.screen.update_screen()

            clock.tick(constants.FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION:
                if self.one_player_button.is_mouse_over(mouse_position):
                    self.one_player_button.hover()
                else:
                    self.one_player_button.unhover()
                if self.multi_player_button.is_mouse_over(mouse_position):
                    self.multi_player_button.hover()
                else:
                    self.multi_player_button.unhover()

            if event.type == pygame.MOUSEBUTTONDOWN and self.one_player_button.is_mouse_over(mouse_position):
                self.mode = GameModes.SINGLE

            if event.type == pygame.MOUSEBUTTONDOWN and self.multi_player_button.is_mouse_over(mouse_position):
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




class GameModes(Enum):
    SINGLE = 1
    MULTI = 2
