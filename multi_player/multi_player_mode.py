import pygame
from . import multi_player_assets
from . import network
import constants
from game_objects import bird, bird_color, pipe_manager
from sound import sound_loader, sound_names
import sys


pygame.init()

SPAWN_PIPE_EVENT = pygame.USEREVENT
COLLIDE_EVENT = pygame.USEREVENT + 1
OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2
BIRD_FLAP_EVENT = pygame.USEREVENT + 3

pygame.time.set_timer(SPAWN_PIPE_EVENT, 1400)
pygame.time.set_timer(BIRD_FLAP_EVENT, 150)


class MultiPlayerMode:

    def __init__(self, screen, clock, landscape):
        self.screen = screen
        self.clock = clock
        self.landscape = landscape
        self.network = network.Network()
        self.player_id = self.network.get_player_id()
        self.player = bird.Bird(
            initial_pos=(180,0), color=bird_color.BirdColor.RED)     # 355
        self.opponent = bird.Bird(
            initial_pos=(100,0), color=bird_color.BirdColor.BLUE)
        self.pipe_manager = pipe_manager.PipeManager()
        self.back_to_home_button = multi_player_assets.BackToHomeButton()
        self.sounds = sound_loader.SoundLoader()
        self.game_speed = constants.GAME_SPEED
        self.is_game_active = True
        self.run = True
        self.run_game()


    def run_game(self):
        player_id = int(self.player_id) + 1
        print(f'You are player {player_id}')

        while self.run:

            # # ask server to send us the game
            # try:
            #     game = self.network.send('game')
            # # Someone disconnected
            # except:
            #     self.run = False

            game = self.network.send('game')
            if game.are_both_connected():
                player_y = self.player.get_bird_y()
                opponent_y = int(self.network.send(str(player_y)))
                self.opponent.update_bird_y(opponent_y)

            self.check_collision()
            self.check_out_of_bounds()
            self.check_events(game)
            self.move_objects(game)
            self.draw_objects()
            self.screen.update_screen()

            self.clock.tick(constants.FPS)


    def check_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.is_game_active and game.are_both_connected():
                if event.type == SPAWN_PIPE_EVENT:
                    self.pipe_manager.add_pipe(
                        constants.SCREEN_WIDTH, constants.PIPE_GAP)

                if (event.type == COLLIDE_EVENT
                        or event.type == OUT_OF_BOUNDS_EVENT):
                    self.is_game_active = False
                    self.sounds.play_sound(sound_names.SoundNames.COLLIDE)

                if event.type == BIRD_FLAP_EVENT:
                    self.player.change_bird_frame()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.is_game_active and game.are_both_connected():
                self.player.on_tap(constants.JUMP_VELOCITY)
                self.sounds.play_sound(sound_names.SoundNames.FLAP)

            mouse_position = pygame.mouse.get_pos()

            # Fill button with specified color when button is hovered
            if event.type == pygame.MOUSEMOTION:
                self.back_to_home_button.fill_back_to_home_button(mouse_position)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_to_home_button.is_mouse_over(mouse_position):
                    self.run = False


    def draw_objects(self):
        screen = self.screen.get_screen()
        self.landscape.draw_background(screen)
        self.landscape.draw_foreground(screen)
        self.pipe_manager.draw_pipes(screen)
        self.player.draw_bird(screen)
        self.opponent.draw_bird(screen)

        if not self.is_game_active:
            self.back_to_home_button.draw_back_to_home_button(screen)


    def move_objects(self, game):
        if self.is_game_active:
            self.landscape.move_foreground(self.game_speed)
            self.pipe_manager.move_pipes(self.game_speed)
            if game.are_both_connected():
                self.player.move_bird(constants.GRAVITY)
        else:
            self.player.fall(constants.FLOOR_HEIGHT, constants.FALL_RATE)


    def check_collision(self):
        bird_rect = self.player.get_bird_rect()
        for pipe in self.pipe_manager.get_individual_pipes():
            pipe_rect = pipe.get_pipe_rect()
            if bird_rect.colliderect(pipe_rect):
                pygame.event.post(pygame.event.Event(COLLIDE_EVENT))


    def check_out_of_bounds(self):
        bird_rect = self.player.get_bird_rect()
        if bird_rect.bottom >= constants.FLOOR_HEIGHT:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS_EVENT))


    def reset_game(self):
        self.is_game_active = True
        self.run = True
        self.pipe_manager.clear_pipes()
        self.player.reset_bird()
