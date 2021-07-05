import pygame
import constants
from creation import image_loader, button_creator


class StartText:

    def __init__(self, screen_width):
        self.start = image_loader.ImageLoader.load_image('start.png')
        self.start = pygame.transform.scale(self.start, (385,95))
        self.start_rect = self.start.get_rect(center=(screen_width // 2, 150))


    def draw_start(self, screen):
        screen.blit(self.start, self.start_rect)



class GameOverText:

    def __init__(self, screen_width):
        self.game_over = image_loader.ImageLoader.load_image('gameover.png')
        self.game_over = pygame.transform.scale(self.game_over, (360,80))
        self.game_over_rect = self.game_over.get_rect(
            center=(screen_width // 2, 190))


    def draw_game_over(self, screen):
        screen.blit(self.game_over, self.game_over_rect)



class RestartButton:

    def __init__(self):
        self.restart_button = button_creator.ButtonCreator(
            x=88, y=330, width=330, height=50, size=37, text='Restart',
            color_text=constants.BLACK, color_fill=constants.YELLOW)


    def draw_restart_button(self, screen):
        self.restart_button.draw(screen)


    def is_mouse_over(self, position):
        return self.restart_button.is_mouse_over(position)


    def fill_restart_button(self, position):
        if self.is_mouse_over(position):
            self.restart_button.change_color_fill(constants.GREEN)
        else:
            self.restart_button.change_color_fill(constants.YELLOW)



class BackToHomeButton:

    def __init__(self):
        self.back_to_home_button = button_creator.ButtonCreator(
            x=88, y=400, width=330, height=50, size=37, text='Back to Home',
            color_text=constants.BLACK, color_fill=constants.YELLOW)


    def draw_back_to_home_button(self, screen):
        self.back_to_home_button.draw(screen)


    def is_mouse_over(self, position):
        return self.back_to_home_button.is_mouse_over(position)


    def fill_back_to_home_button(self, position):
        if self.is_mouse_over(position):
            self.back_to_home_button.change_color_fill(constants.GREEN)
        else:
            self.back_to_home_button.change_color_fill(constants.YELLOW)
