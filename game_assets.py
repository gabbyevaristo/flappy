import pygame
import constants
from creation import button_creator, image_loader


class Logo:

    def __init__(self, screen_width):
        self.logo = image_loader.ImageLoader.load_image('logo.png')
        self.logo = pygame.transform.scale(self.logo, (385,135))
        self.logo_rect = self.logo.get_rect(center=(screen_width // 2, 190))


    def draw_logo(self, screen):
        screen.blit(self.logo, self.logo_rect)



class OnePlayerButton:

    def __init__(self):
        self.one_player_button = button_creator.ButtonCreator(
            x=130, y=440, width=240, height=50, size=40, text='1 Player',
            color_text=constants.BLACK, color_fill=constants.YELLOW)


    def draw_one_player_button(self, screen):
        self.one_player_button.draw(screen)


    def is_mouse_over(self, position):
        return self.one_player_button.is_mouse_over(position)


    def fill_one_player_button(self, position):
        if self.is_mouse_over(position):
            self.one_player_button.change_color_fill(constants.GREEN)
        else:
            self.one_player_button.change_color_fill(constants.YELLOW)



class MultiPlayerButton:

    def __init__(self):
        self.multi_player_button = button_creator.ButtonCreator(
            x=130, y=510, width=240, height=50, size=40, text='2 Player',
            color_text=constants.BLACK, color_fill=constants.YELLOW)


    def draw_multi_player_button(self, screen):
        self.multi_player_button.draw(screen)


    def is_mouse_over(self, position):
        return self.multi_player_button.is_mouse_over(position)


    def fill_multi_player_button(self, position):
        if self.is_mouse_over(position):
            self.multi_player_button.change_color_fill(constants.GREEN)
        else:
            self.multi_player_button.change_color_fill(constants.YELLOW)
