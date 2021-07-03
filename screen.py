import pygame


class Screen:

    def __init__(self, width, height, name='Flappy Bird'):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

    def update_screen(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    """Solves quadratic equations using the quadratic formula.

    Args:
        a: the first coefficient.
        b: the second coefficient.
        c: the third coefficient.
        disc: the discriminant of the function.
    Returns:
        the roots of the quadratic equation.

    """

    """
    test_function does blah blah blah.

    :param p1: describe about parameter p1
    :param p2: describe about parameter p2
    :param p3: describe about parameter p3
    :return: describe what it returns
    """