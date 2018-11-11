import pygame

class CenteredText(object):
    """
    Class representing centered text
    """

    def __init__(self, text_, size_, color_):
        self.text = text_
        self.size = size_
        self.color = color_
        myfont = pygame.font.SysFont('Comic Sans MS', self.size)
        self.text_surface = myfont.render(self.text, False, self.color)


    def get_width(self):
        return self.text_surface.get_width()


    def get_height(self):
        return self.text_surface.get_height()


    def _get_text_location(self, window):
        x = (window.get_width() - self.get_width()) / 2
        y = window.get_height()/2 - 2*self.get_height()
        return (x, y)


    def write(self, window):
        window.blit(self.text_surface, self._get_text_location(window))