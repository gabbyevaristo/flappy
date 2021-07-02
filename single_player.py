import pygame
import constants
import canvas
import landscape
import bird
import pipes
import score
import text
import os
import sys
import image_loader
import time


# on home screen, up to go to single player -> replace w button
# on single player, up to restart           -> replace w button
# on single player, left to go back to home page -> replace w button



pygame.init()

# event_index = 0

# event triggered by timer
SPAWN_PIPE_EVENT = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE_EVENT, 1400)

COLLIDE_EVENT = pygame.USEREVENT + 1

OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2

BIRD_FLAP_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(BIRD_FLAP_EVENT, 150)

PASSED_EVENT = pygame.USEREVENT + 4



class SinglePlayer:

    def __init__(self, screen, landscape, clock):
        self.screen = screen
        self.landscape = landscape
        self.player = bird.Bird(constants.JUMP_VELOCITY)
        self.pipes = pipes.Pipes()
        self.game_speed = constants.INIT_GAME_SPEED
        self.game_active = False
        self.show_start = True
        self.is_game_over = False
        self.run = True
        self.start = image_loader.ImageLoader.load_image('press-to-start.png')
        self.start = pygame.transform.scale(self.start, (385,95))
        self.game_over = image_loader.ImageLoader.load_image('game-over.png')
        self.game_over = pygame.transform.scale(self.game_over, (385,120))
        self.clock = clock
        self.score = score.Score()
        self.run_game()

    def run_game(self):
        # clock = pygame.time.Clock()
        while self.run:
            self.check_collision()
            self.check_in_bounds()
            self.check_passed()
            self.check_events()
            self.move_objects()
            self.draw_objects()
            self.screen.update_screen()

            self.clock.tick(constants.FPS)

    def draw_objects(self):
        # Background
        background = self.landscape.get_background()
        self.screen.draw(background, (0, 0))

        # Pipes
        for pipe in self.pipes.get_pipes():
            pipe_surface = self.pipes.get_pipe(pipe)
            self.screen.draw(pipe_surface, pipe)

        # Bird
        self.screen.draw(self.player.rotate_bird(), self.player.get_bird_rect())

        # Foreground
        foreground, foreground_x = self.landscape.get_foreground(), self.landscape.get_foreground_x()
        self.screen.draw(foreground, (foreground_x, constants.FLOOR_HEIGHT))
        self.screen.draw(foreground, (foreground_x + self.landscape.get_foreground_width(), constants.FLOOR_HEIGHT))

        if self.show_start:
            self.screen.draw(self.start, (55,150))

        if self.game_active:
            score_surface, score_rect = self.score.get_score_surface(), self.score.get_score_rect()
            self.screen.draw(score_surface, score_rect)

        if self.is_game_over:
            self.screen.draw(self.game_over, (55,150))


    def move_objects(self):
        if self.game_active:
            # Player
            self.player.move_bird(constants.GRAVITY)

            # Pipes
            self.pipes.move_pipes(self.game_speed)

            # Foreground
            self.landscape.move_foreground(self.game_speed)

        if self.is_game_over:
            # Player fall
            bird_rect = self.player.get_bird_rect()
            if bird_rect.bottom < constants.FLOOR_HEIGHT:
                self.player.fall()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SPAWN_PIPE_EVENT and self.game_active:
                self.pipes.add_pipe()

            if event.type == COLLIDE_EVENT:
                self.is_game_over = True
                self.game_active = False

            if event.type == OUT_OF_BOUNDS_EVENT:
                self.is_game_over = True
                self.game_active = False

            if event.type == BIRD_FLAP_EVENT and self.game_active:
                self.player.change_bird_frame()

            if event.type == PASSED_EVENT and self.game_active:
                self.score.update_current_score()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.is_game_over:
                self.game_active = True
                self.show_start = False
                self.player.on_tap()

            # restart the game
            if keys[pygame.K_UP] and self.is_game_over:
                self.reset_game()

            # go back to home page
            if keys[pygame.K_LEFT] and not self.game_active:
                self.run = False

    def check_collision(self):
        for pipe in self.pipes.get_pipes():
            bird_rect = self.player.get_bird_rect()
            if bird_rect.colliderect(pipe):
                pygame.event.post(pygame.event.Event(COLLIDE_EVENT))

    def check_in_bounds(self):
        bird_rect = self.player.get_bird_rect()
        if bird_rect.bottom >= 660:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS_EVENT))

    def check_passed(self):
        for pipe in self.pipes.get_pipes():
            bird_rect = self.player.get_bird_rect()
            if bird_rect.left - self.pipes.get_pipe_width() <= pipe.right <= bird_rect.left:
                pygame.event.post(pygame.event.Event(PASSED_EVENT))

    def reset_game(self):
        self.show_start = True
        self.is_game_over = False
        self.run = True
        self.pipes.clear_pipes()
        self.player.reset_bird()
