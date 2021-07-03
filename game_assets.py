import pygame
import button_creator
import image_loader
import constants


class Logo:

    def __init__(self):
        self.logo = image_loader.ImageLoader.load_image('logo.png')
        self.logo = pygame.transform.scale(self.logo, (385,135))

    def draw_logo(self, screen):
        screen.blit(self.logo, (60,150))



class OnePlayerButton:

    def __init__(self):
        self.one_player_button = button_creator.ButtonCreator(x=130, y=440, width=240, height=50, text='1 Player', color_text=constants.BLACK, color_fill=constants.YELLOW, size=40)

    def draw_one_player_button(self, screen):
        self.one_player_button.draw(screen)

    def is_mouse_over(self, position):
        return self.one_player_button.is_mouse_over(position)

    def hover(self):
        self.one_player_button.change_color_fill(constants.GREEN)

    def unhover(self):
        self.one_player_button.change_color_fill(constants.YELLOW)


class MultiPlayerButton:

    def __init__(self):
        self.multi_player_button = button_creator.ButtonCreator(x=130, y=510, width=240, height=50, text='2 Player', color_text=constants.BLACK, color_fill=constants.YELLOW, size=40)

    def draw_multi_player_button(self, screen):
        self.multi_player_button.draw(screen)

    def is_mouse_over(self, position):
        return self.multi_player_button.is_mouse_over(position)

    def hover(self):
        self.multi_player_button.change_color_fill(constants.GREEN)

    def unhover(self):
        self.multi_player_button.change_color_fill(constants.YELLOW)
