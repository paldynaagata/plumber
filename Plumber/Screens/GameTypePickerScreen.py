import pygame
import Localization

from Screens.MenuScreen import MenuScreen
from Screens.GameScreen import GameScreen
from UIItems.Button import Button

class GameTypePickerScreen(MenuScreen):
    """
    Class representing menu screen for all types of boards,
    inherited class MenuScreen
    """

    def __init__(self, title_key, screen_getter):
        board_3x3 = Button("3 x 3")
        board_3x3.set_click(lambda: screen_getter('3x3'))

        board_4x4 = Button("4 x 4")
        board_4x4.set_click(lambda: screen_getter('4x4'))

        board_5x5 = Button("5 x 5")
        board_5x5.set_click(lambda: screen_getter('5x5'))

        back_button = Button(Localization.get_text('back'))
        back_button.set_click(lambda: MainMenuScreen())

        buttons = (board_3x3, board_4x4, board_5x5, back_button)

        super().__init__(buttons, Localization.get_text(title_key), 60)


from Screens.MainMenuScreen import MainMenuScreen
# it is here because modules import each other