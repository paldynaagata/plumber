import pygame
import Sounds
import Settings

from pygame import Rect
from UIItems.CenteredText import CenteredText

class Button:
    """
    Class representing a button
    """

    def __init__(self, text):
        self.text = None
        self.click_method = None
        self.rect = None
        self._scale_factor = Settings.get_scale_factor()
        self.size = (int(170 * self._scale_factor), int(50 * self._scale_factor))
        self.set_text(text)


    def set_text(self, text):
        self.text = CenteredText(text, 20 * self._scale_factor, (0, 0, 0))


    def set_click(self, method):
        self.click_method = method


    def on_click(self):
        Sounds.play_button_click()
        return None if self.click_method is None else self.click_method()


    def draw(self, window, color, location):
        self.rect = pygame.draw.rect(window, color, Rect(location, self.size))
        self.text.write(window, self.rect)