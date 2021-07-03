import pygame
import text
import constants



class Score:
    def __init__(self):
        self.current_score = 0
        self.high_score = 0
        self.score_text = text.Text(size=85, text=str(self.current_score), color=constants.BLACK, position=(constants.SCREEN_WIDTH // 2,150))

    def update_current_score(self):
        self.current_score += 1
        self.score_text.change_text(str(self.current_score))

    def get_score_surface(self):
        return self.score_text.get_font_surface()

    def get_score_rect(self):
        return self.score_text.get_font_rect()
