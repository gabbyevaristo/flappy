import pygame
import constants
from creation import text_creator


class Score:

    def __init__(self, screen_width):
        self.current_score = 0
        self.current_score_text = text_creator.TextCreator(
            position=(screen_width // 2, 150), size=85, text='0',
            color=constants.BLACK)
        self.final_score_text = text_creator.TextCreator(
            position=(screen_width // 2, 600), size=45, text='',
            color=constants.BLACK)


    def draw_current_score(self, screen):
        current_score_surface = self.current_score_text.get_text_surface()
        current_score_rect = self.current_score_text.get_text_rect()
        screen.blit(current_score_surface, current_score_rect)


    def draw_final_score(self, screen):
        self.update_final_score()
        final_score_surface = self.final_score_text.get_text_surface()
        final_score_rect = self.final_score_text.get_text_rect()
        screen.blit(final_score_surface, final_score_rect)


    def update_current_score(self):
        self.current_score += 1
        self.current_score_text.update_text(self.current_score)


    def update_final_score(self):
        self.final_score_text.update_text(f'Score {self.current_score}')


    def reset_score(self):
        self.current_score = 0
        self.current_score_text.update_text(self.current_score)
