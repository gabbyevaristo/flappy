import pygame
from . import multi_player_assets
from . import network
import game_modes
import constants
from game_objects import bird, bird_color, pipe_manager
from sound import sound_loader, sound_names
import sys


pygame.init()

SPAWN_PIPE_EVENT = pygame.USEREVENT
COLLIDE_EVENT = pygame.USEREVENT + 1
OUT_OF_BOUNDS_EVENT = pygame.USEREVENT + 2
BIRD_FLAP_EVENT = pygame.USEREVENT + 3

pygame.time.set_timer(BIRD_FLAP_EVENT, 150)


class MultiPlayerMode:

    def __init__(self, screen, landscape):
        self.screen = screen
        self.clock = None
        self.landscape = landscape
        self.network = network.Network()
        self.player_id = self.network.get_player_id()
        self.player = bird.Bird(
            initial_pos=(180,255), color=bird_color.BirdColor.RED)
        self.opponent = bird.Bird(
            initial_pos=(180,255), color=bird_color.BirdColor.BLUE)
        self.pipe_manager = pipe_manager.PipeManager(game_modes.GameModes.MULTI)
        self.waiting_text = multi_player_assets.WaitingForOpponentText(
            constants.SCREEN_WIDTH)
        self.winner_text = multi_player_assets.WinnerText(constants.SCREEN_WIDTH)
        self.loser_text = multi_player_assets.LoserText(constants.SCREEN_WIDTH)
        self.rematch_button = multi_player_assets.RematchButton()
        self.back_to_home_button = multi_player_assets.BackToHomeButton()
        self.sounds = sound_loader.SoundLoader()
        self.game_speed = constants.GAME_SPEED
        self.show_start = True
        self.is_game_active = False
        self.are_both_connected = False
        self.spawn_event = False
        # self.rematch = False
        self.run = True
        self.winner = None
        self.run_game()


    def run_game(self):
        player_id = self.player_id + 1
        print(f'You are player {player_id}')

        self.clock = pygame.time.Clock()
        while self.run:
            self.send_position()
            self.check_collision()
            self.check_out_of_bounds()
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

            # if self.is_game_active and self.are_both_connected and self.rematch:
            if self.is_game_active and self.are_both_connected:
                if event.type == SPAWN_PIPE_EVENT:
                    self.pipe_manager.add_pipe(
                        constants.SCREEN_WIDTH, constants.PIPE_GAP)

                if (event.type == COLLIDE_EVENT
                        or event.type == OUT_OF_BOUNDS_EVENT):
                    self.is_game_active = False
                    self.network.send('collide')
                    self.sounds.play_sound(sound_names.SoundNames.COLLIDE)

                if event.type == BIRD_FLAP_EVENT:
                    self.player.change_bird_frame()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    self.player.on_tap(constants.JUMP_VELOCITY)
                    self.sounds.play_sound(sound_names.SoundNames.FLAP)

            mouse_position = pygame.mouse.get_pos()

            # Fill button with specified color when button is hovered
            if event.type == pygame.MOUSEMOTION:
                self.rematch_button.fill_rematch_button(mouse_position)
                self.back_to_home_button.fill_back_to_home_button(mouse_position)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rematch_button.is_mouse_over(mouse_position):
                    self.network.send('rematch')
                    self.reset_game()
                if self.back_to_home_button.is_mouse_over(mouse_position):
                    self.run = False


    def draw_objects(self):
        screen = self.screen.get_screen()
        self.landscape.draw_background(screen)
        self.landscape.draw_foreground(screen)
        self.pipe_manager.draw_pipes(screen)
        self.player.draw_bird(screen)

        # if (self.are_both_connected and self.rematch) or not self.is_game_active:
        if self.are_both_connected:
            self.opponent.draw_bird(screen)
        else:
            self.waiting_text.draw_waiting_text(screen)

        if not self.show_start and not self.is_game_active:
            if self.player_id == self.winner:
                self.winner_text.draw_winner_text(screen)
            else:
                self.loser_text.draw_loser_text(screen)
            self.rematch_button.draw_rematch_button(screen)
            self.back_to_home_button.draw_back_to_home_button(screen)


    def move_objects(self):
        # if self.are_both_connected and self.rematch:
        if self.are_both_connected:
            if self.is_game_active:
                self.landscape.move_foreground(self.game_speed)
                self.pipe_manager.move_pipes(self.game_speed)
                self.player.move_bird(constants.GRAVITY)
            else:
                # The winner freezes while the loser falls to the ground
                if self.player_id == self.winner:
                    self.opponent.fall(constants.FLOOR_HEIGHT, constants.FALL_RATE)
                else:
                    self.player.fall(constants.FLOOR_HEIGHT, constants.FALL_RATE)


    def send_position(self):
        try:
            game = self.network.send('game')
        except:
            self.run = False
            print('Could not get game')
        else:
            if game:
                if game.are_both_connected():
                    self.are_both_connected = True
                    self.is_game_active = True
                    if not self.spawn_event:
                        self.spawn_event = True
                        pygame.time.set_timer(SPAWN_PIPE_EVENT, 1500)

                    # if game.get_rematch():
                    #     self.rematch = True

                    # If there is no winner yet, grab the opponent's move
                    if game.get_winner() == None:
                        self.show_start = False
                        player_y = self.player.get_bird_y()
                        self.network.send(str(player_y))
                        opponent_y = game.get_opponent_y(self.player_id)
                        self.opponent.update_bird_y(opponent_y)
                    else:
                        # self.network.send('gameover')
                        self.is_game_active = False
                        # self.rematch = False
                        self.winner = game.get_winner()
            else:
                self.run = False


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
        self.pipe_manager.clear_pipes()
        self.player.reset_bird()
        self.opponent.reset_bird()
