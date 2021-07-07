import pygame
import constants
from creation import button_creator, text_creator


class WaitingForOpponentText:

    def __init__(self, screen_width):
        self.waiting_text = text_creator.TextCreator(
            position=(screen_width // 2, 400), size=38,
            text='Waiting for Opponent', color=constants.BLACK)


    def draw_waiting_text(self, screen):
        waiting_text_surface = self.waiting_text.get_text_surface()
        waiting_text_rect = self.waiting_text.get_text_rect()
        screen.blit(waiting_text_surface, waiting_text_rect)



class WinnerText:

    def __init__(self, screen_width):
        self.winner_text = text_creator.TextCreator(
            position=(screen_width // 2, 200), size=85, text='You Win',
            color=constants.BLACK)


    def draw_winner_text(self, screen):
        winner_text_surface = self.winner_text.get_text_surface()
        winner_text_rect = self.winner_text.get_text_rect()
        screen.blit(winner_text_surface, winner_text_rect)



class LoserText:

    def __init__(self, screen_width):
        self.loser_text = text_creator.TextCreator(
            position=(screen_width // 2, 200), size=85, text='You Lose',
            color=constants.BLACK)


    def draw_loser_text(self, screen):
        loser_text_surface = self.loser_text.get_text_surface()
        loser_text_rect = self.loser_text.get_text_rect()
        screen.blit(loser_text_surface, loser_text_rect)



class BackToHomeButton:

    def __init__(self):
        self.back_to_home_button = button_creator.ButtonCreator(
            x=88, y=470, width=330, height=50, size=37, text='Back to Home',
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
