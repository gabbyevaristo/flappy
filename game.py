import pygame
import constants
import canvas
import background
import player
import os

pygame.init()


class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = canvas.Canvas(self.width, self.height)
        self.background = background.Background()
        self.player1 = player.Player()
        self.index = 0
        # self.objects = []
        # self.append_objects()

    def run_game(self):
        clock = pygame.time.Clock()
        speed = 60
        run = True

        while run:
            clock.tick(speed)

            if self.check_events() == False:
                run = False
            self.background.move_background(1.4)
            self.screen.draw_background(self.background.get_background(), self.background.get_background_x1(), self.background.get_background_x2())
            # self.screen.draw_objects(self.objects)

            self.screen.draw(self.player1.get_player_sprites()[self.index], (20,20))

            self.screen.update_screen()

        pygame.quit()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.index = (self.index + 1) % len(self.player1.get_player_sprites())

    # def append_objects(self):
    #     self.objects.append(self.player1)
