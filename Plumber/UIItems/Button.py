import pygame

from pygame import Rect
from UIItems.CenteredText import CenteredText

class Button:
    """
    Class representing a button
    """

    def __init__(self, text):
        self.text = CenteredText(text, 20, (0, 0, 0))
        self.size = (150, 50)
        self.click_method = None
        self.rect = None


    def set_click(self, method):
        self.click_method = method


    def on_click(self):
        return None if self.click_method is None else self.click_method()


    def draw(self, window, color, location):
        self.rect = pygame.draw.rect(window, color, Rect(location, self.size))
        self.text.write(window, self.rect)