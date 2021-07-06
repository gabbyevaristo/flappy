import pygame
import constants
from creation import button_creator


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
