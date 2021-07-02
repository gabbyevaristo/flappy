import pygame
import constants
import canvas
import landscape
import player
import pipes
import os
import sys

pygame.init()

# event_index = 0

# event triggered by timer
SPAWN_PIPE_EVENT = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE_EVENT, 1600)

COLLIDE_EVENT = pygame.USEREVENT + 1
OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2



class Game:

    def __init__(self):
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT
        self.screen = canvas.Canvas(self.width, self.height)
        self.landscape = landscape.Landscape()
        self.player1 = player.Player(constants.JUMP_VELOCITY)
        self.pipes = pipes.Pipes()
        self.game_speed = constants.INIT_GAME_SPEED
        self.game_active = True

    def run_game(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            self.check_collision()
            self.check_in_bounds()
            self.check_events()
            self.move_objects()
            self.draw_objects()
            self.screen.update_screen()

            clock.tick(constants.FPS)

    def draw_objects(self):
        # Background
        background = self.landscape.get_background()
        self.screen.draw(background, (0, 0))

        # Pipes
        for pipe in self.pipes.get_pipes():
            pipe_surface = self.pipes.get_pipe(pipe)
            self.screen.draw(pipe_surface, pipe)

        # Player
        player_surface, player_rect = self.player1.get_player()
        self.screen.draw(player_surface, player_rect)

        # Foreground
        foreground, foreground_x = self.landscape.get_foreground(), self.landscape.get_foreground_x()
        self.screen.draw(foreground, (foreground_x, constants.FLOOR_HEIGHT))
        self.screen.draw(foreground, (foreground_x + self.landscape.get_foreground_width(), constants.FLOOR_HEIGHT))

    def move_objects(self):
        if self.game_active:
            # Player
            self.player1.move_player(constants.GRAVITY)

            # Pipes
            self.pipes.move_pipes(self.game_speed)

            # Foreground
            self.landscape.move_foreground(self.game_speed)
        else:
            # Player fall
            _, player_rect = self.player1.get_player()
            if player_rect.bottom <= constants.FLOOR_HEIGHT:
                self.player1.fall()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SPAWN_PIPE_EVENT:
                self.pipes.add_pipe()

            if event.type == COLLIDE_EVENT:
                self.game_active = False

            if event.type == OUT_OF_BOUNDS_EVENT:
                self.game_active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.player1.on_tap()

    def check_collision(self):
        for pipe in self.pipes.get_pipes():
            _, player_rect = self.player1.get_player()
            if player_rect.colliderect(pipe):
                pygame.event.post(pygame.event.Event(COLLIDE_EVENT))

    def check_in_bounds(self):
        _, player_rect = self.player1.get_player()
        if player_rect.bottom >= 660:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS_EVENT))

