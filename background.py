import image_loader


BACKGROUND_FILE= 'background.jpg'

class Background:

    def __init__(self):
        self.background = image_loader.ImageLoader.load_image(BACKGROUND_FILE)
        self.background_x1 = 0
        self.background_x2 = self.background.get_width()

    def move_background(self, speed):
        x1 = self.get_background_x1()
        x2 = self.get_background_x2()
        self.set_background_x1(x1 - speed)
        self.set_background_x2(x2 - speed)

        if x1 < self.background.get_width() * -1:  # If the bg is at the -width, then reset its position
            self.set_background_x1(self.background.get_width())

        if x2 < self.background.get_width() * -1:
            self.set_background_x2(self.background.get_width())

    def get_background(self):
        return self.background

    def get_background_x1(self):
        return self.background_x1

    def get_background_x2(self):
        return self.background_x2

    def set_background_x1(self, x):
        self.background_x1 = x

    def set_background_x2(self, x):
        self.background_x2 = x
