import pygame
import Constants

class CenteredText(object):
    """
    Class representing text centered horizontal
    """

    def __init__(self, text_, size_, color_):
        self.text = text_
        self.size = size_
        self.color = color_
        myfont = pygame.font.SysFont(Constants.font, self.size)
        self.text_surface = myfont.render(self.text, False, self.color)


    def get_width(self):
        return self.text_surface.get_width()


    def get_height(self):
        return self.text_surface.get_height()


    def _get_text_location(self, rect):
        x = rect.left + (rect.width - self.get_width()) / 2
        y = rect.top + (rect.height - self.get_height()) / 2
        return x, y


    def write(self, window, rect = None, y = None):
        if rect is None:
            rect = window.get_rect()

        x, centered_y = self._get_text_location(rect)
        if y is None:
            y = centered_y

        window.blit(self.text_surface, (x, y))