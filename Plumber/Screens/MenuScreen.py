import pygame

from abc import ABCMeta, abstractmethod
from Screens.Screen import Screen
from UIItems.CenteredText import CenteredText

class MenuScreen(Screen, metaclass = ABCMeta):
    """
    Class representing a menu screen
    """

    @abstractmethod
    def __init__(self, buttons, header, header_size):
        self.title = CenteredText(header, header_size, (255, 153, 153))
        self.button_color = (255, 255, 102)
        self.buttons = buttons


    def show(self, game):
        self.title.write(game.window, y = game.window.get_height() / 3 - 2.5 * self.title.size)

        i = 2 * len(self.buttons)
        
        for button in self.buttons:
            x = (game.window.get_width() - button.size[0]) / 2
            y = game.window.get_height() - i * button.size[1]
            button.draw(game.window, self.button_color, (x, y))
            i -= 2

        for event in game.events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_point = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(mouse_point):
                        if button.click_method is not None:
                            screen = button.on_click()
                            return screen
                        break

        return super().show(game)