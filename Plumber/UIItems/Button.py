import pygame
from pygame import Rect

class Button:
    """
    Class representing a button
    """

    def __init__(self, name_):
        self.name = name_
        self.size = (150, 50)
        self.click_method = None
        self.rect = None
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.text_surface = myfont.render(self.name, False, (0, 0, 0))


    def set_click(self, method):
        self.click_method = method


    def on_click(self):
        return None if self.click_method is None else self.click_method()


    def get_width(self):
        return self.text_surface.get_width()


    def get_height(self):
        return self.text_surface.get_height()


    def _get_text_location(self, rect, location):
        x = location[0] + (rect.width - self.get_width()) // 2
        y = location[1] + (rect.height - self.get_height()) // 2
        return (x, y)


    def draw(self, window, color, location):
        self.rect = pygame.draw.rect(window, color, Rect(location, self.size))
        window.blit(self.text_surface, self._get_text_location(self.rect, location))