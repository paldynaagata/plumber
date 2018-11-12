import pygame
import Localization

from Screens.MenuScreen import MenuScreen
from Screens.GameScreen import GameScreen
from UIItems.Button import Button

class NewGameMenuScreen(MenuScreen):
    """
    Class representing new game menu screen,
    inherited class Screen
    """

    def __init__(self):
        board_3x3 = Button("3 x 3")
        board_3x3.set_click(lambda: GameScreen('Boards/boards_3x3.txt'))

        board_4x4 = Button("4 x 4")
        board_4x4.set_click(lambda: GameScreen('Boards/boards_4x4.txt'))

        board_5x5 = Button("5 x 5")
        board_5x5.set_click(lambda: GameScreen('Boards/boards_5x5.txt'))

        back_button = Button(Localization.get_text('back'))
        back_button.set_click(lambda: MainMenuScreen())

        buttons = (board_3x3, board_4x4, board_5x5, back_button)

        super().__init__(buttons, Localization.get_text('choose_size'), 60)

from Screens.MainMenuScreen import MainMenuScreen
# it is here because modules import each other