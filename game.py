import pygame
import constants
import canvas
import background
import player
import os
import sys

pygame.init()

x, y = 140, 355
is_jump = False
jump_count = 10

class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = canvas.Canvas(self.width, self.height)
        self.background = background.Background()
        self.player1 = player.Player()
        self.index = 0

    def run_game(self):
        clock = pygame.time.Clock()
        speed = 60
        run = True

        while run:
            clock.tick(speed)

            if self.check_events() == False:
                run = False
                pygame.quit()
                sys.exit()

            self.background.move_background(1.4)
            self.screen.draw_background(self.background.get_background(), self.background.get_background_x1(), self.background.get_background_x2())

            cur_player = self.player1.get_player_sprites()[self.index]
            self.screen.draw(cur_player, (x,y))

            self.screen.update_screen()


    def check_events(self):
        global x,y,is_jump,jump_count
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.index = (self.index + 1) % len(self.player1.get_player_sprites())
