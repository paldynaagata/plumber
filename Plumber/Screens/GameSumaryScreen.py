import pygame
import Localization

from Scores import Scores
from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText

class GameSummaryScreen(MenuScreen):
    """
    Class representing summary of the game screen,
    inherited class MenuScreen
    """

    def __init__(self, click_count, board_size):
        self.click_count = click_count
        self.board_size = board_size

        scores = Scores(f"{self.board_size}x{self.board_size}")
        scores.add_score('User', self.click_count)

        menu_button = Button(Localization.get_text('menu'))
        menu_button.set_click(lambda: MainMenuScreen())

        buttons = [menu_button]


        super().__init__(buttons, Localization.get_text('congratulations'), 60)


    def show(self, game):
        text_ = str.format("{0} {1}.", Localization.get_text('score'), self.click_count)
        text = CenteredText(text_, 40, (0, 0, 0))
        text.write(game.window, y = game.window.get_height() / 2 - 2 * text.size)

        return super().show(game)


from Screens.MainMenuScreen import MainMenuScreen