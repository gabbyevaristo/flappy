import pygame
import constants
import landscape
import bird
import pipe_manager
import score
import single_player_assets
import sys


# on home screen, up to go to single player -> replace w button
# on single player, up to restart           -> replace w button
# on single player, left to go back to home page -> replace w button

pygame.init()

SPAWN_PIPE_EVENT = pygame.USEREVENT
COLLIDE_EVENT = pygame.USEREVENT + 1
OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2
BIRD_FLAP_EVENT = pygame.USEREVENT + 3
PASSED_EVENT = pygame.USEREVENT + 4

pygame.time.set_timer(SPAWN_PIPE_EVENT, 1400)
pygame.time.set_timer(BIRD_FLAP_EVENT, 150)


class SinglePlayer:

    def __init__(self, screen, landscape, clock):
        self.screen = screen
        self.clock = clock
        self.landscape = landscape
        self.player = bird.Bird()
        self.pipe_manager = pipe_manager.PipeManager()
        self.game_speed = constants.INIT_GAME_SPEED
        self.start = single_player_assets.StartText()
        self.game_over = single_player_assets.GameOverText()
        self.score = score.Score()
        self.show_start = True
        self.is_game_active = False
        self.is_game_over = False
        self.run = True
        self.run_game()

    def run_game(self):
        while self.run:
            self.check_collision()
            self.check_in_bounds()
            self.check_passed()
            self.check_events()
            self.move_objects()
            self.draw_objects()
            self.screen.update_screen()

            self.clock.tick(constants.FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.is_game_active:
                if event.type == SPAWN_PIPE_EVENT:
                    self.pipe_manager.add_pipe()

                if event.type == COLLIDE_EVENT:
                    self.is_game_over = True
                    self.is_game_active = False

                if event.type == OUT_OF_BOUNDS_EVENT:
                    self.is_game_over = True
                    self.is_game_active = False

                if event.type == BIRD_FLAP_EVENT:
                    self.player.change_bird_frame()

                if event.type == PASSED_EVENT:
                    self.score.update_score()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and not self.is_game_over:
                self.is_game_active = True
                self.show_start = False
                self.player.on_tap()

            # restart the game
            if keys[pygame.K_UP] and self.is_game_over:
                self.reset_game()

            # go back to home page
            if keys[pygame.K_LEFT] and not self.is_game_active:
                self.run = False

    def draw_objects(self):
        screen = self.screen.get_screen()

        self.landscape.draw_background(screen)
        self.landscape.draw_foreground(screen)
        self.pipe_manager.draw_pipes(screen)
        self.player.draw_bird(screen)

        if self.show_start:
            self.start.draw_start(screen)

        if self.is_game_active:
            self.score.draw_current_score(screen)

        if self.is_game_over:
            self.game_over.draw_game_over(screen)
            self.score.draw_final_score(screen)

    def move_objects(self):
        if self.is_game_active:
            self.landscape.move_foreground(self.game_speed)
            self.pipe_manager.move_pipes(self.game_speed)
            self.player.move_bird()

        if self.is_game_over:
            self.player.fall()

    def check_collision(self):
        bird_rect = self.player.get_bird_rect()
        for pipe in self.pipe_manager.get_individual_pipes():
            pipe_rect = pipe.get_pipe_rect()
            if bird_rect.colliderect(pipe_rect):
                pygame.event.post(pygame.event.Event(COLLIDE_EVENT))

    def check_in_bounds(self):
        bird_rect = self.player.get_bird_rect()
        if bird_rect.bottom >= constants.FLOOR_HEIGHT:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS_EVENT))

    def check_passed(self):
        bird_rect = self.player.get_bird_rect()

        for bottom_pipe, top_pipe in self.pipe_manager.get_pipes():
            pipe_rect = bottom_pipe.get_pipe_rect()
            # Only need to check one pipe since top and bottom pipes have the same right position
            if pipe_rect.right <= bird_rect.left and not bottom_pipe.is_pipe_passed():
                bottom_pipe.set_passed_true()
                top_pipe.set_passed_true()
                pygame.event.post(pygame.event.Event(PASSED_EVENT))

    def reset_game(self):
        self.show_start = True
        self.is_game_over = False
        self.run = True
        self.pipe_manager.clear_pipes()
        self.player.reset_bird()
        self.score.reset_score()
