import pygame
import text_creator
import constants


class Score:
    def __init__(self):
        self.current_score = 0
        self.current_score_text = text_creator.TextCreator(size=85, text='0', color=constants.BLACK, position=(constants.SCREEN_WIDTH // 2, 150))
        self.final_score_text = text_creator.TextCreator(size=50, text='', color=constants.BLACK, position=(constants.SCREEN_WIDTH // 2, 400))

    def update_score(self):
        self.current_score += 1
        self.current_score_text.update_text(str(self.current_score))

    def reset_score(self):
        self.current_score = 0
        self.current_score_text.update_text(str(self.current_score))

    def draw_current_score(self, screen):
        screen.blit(self.current_score_text.get_text_surface(), self.current_score_text.get_text_rect())

    def get_final_score_text(self):
        score = str(self.current_score)
        self.final_score_text.update_text(f'Score  {score}')

    def draw_final_score(self, screen):
        self.get_final_score_text()
        screen.blit(self.final_score_text.get_text_surface(), self.final_score_text.get_text_rect())
