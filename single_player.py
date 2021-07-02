import pygame
import constants
import canvas
import landscape
import player
import pipes
import os
import sys
import image_loader

pygame.init()

# event_index = 0

# event triggered by timer
SPAWN_PIPE_EVENT = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE_EVENT, 1600)

COLLIDE_EVENT = pygame.USEREVENT + 1
OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2

# logo = image_loader.ImageLoader.load_image('logo.png')

class SinglePlayer:

    def __init__(self, screen):
        self.screen = screen
        self.landscape = landscape.Landscape()
        self.player1 = player.Player(constants.JUMP_VELOCITY)
        self.pipes = pipes.Pipes()
        self.game_speed = constants.INIT_GAME_SPEED
        self.game_active = False
        self.logo = image_loader.ImageLoader.load_image('logo.png')
        self.logo = pygame.transform.scale(self.logo, (385,135))

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
        self.screen.draw(self.player1.get_player_surface(), self.player1.get_player_rect())

        # Foreground
        foreground, foreground_x = self.landscape.get_foreground(), self.landscape.get_foreground_x()
        self.screen.draw(foreground, (foreground_x, constants.FLOOR_HEIGHT))
        self.screen.draw(foreground, (foreground_x + self.landscape.get_foreground_width(), constants.FLOOR_HEIGHT))

        self.screen.draw(self.logo, (65,150))

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
            player_rect = self.player1.get_player_rect()
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
                # self.reset_game()

            if event.type == OUT_OF_BOUNDS_EVENT:
                self.game_active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.game_active:
                self.player1.on_tap()
            elif keys[pygame.K_SPACE] and not self.game_active:
                self.reset_game()

    def check_collision(self):
        for pipe in self.pipes.get_pipes():
            player_rect = self.player1.get_player_rect()
            if player_rect.colliderect(pipe):
                pygame.event.post(pygame.event.Event(COLLIDE_EVENT))

    def check_in_bounds(self):
        player_rect = self.player1.get_player_rect()
        if player_rect.bottom >= 660:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS_EVENT))

    def reset_game(self):
        self.game_active = True
        self.pipes.clear_pipes()
        self.player1.reset_player()