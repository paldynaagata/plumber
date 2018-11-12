import pygame
import Localization

from Scores import Scores
from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText

class ScoresScreen(MenuScreen):
    """
    Class representing scores screen,
    inherited class MenuScreen
    """

    def __init__(self, board_name):
        self.board_name = board_name
        #scores_3x3 = Scores('3x3')
        #self.scores_3x3 = scores_3x3._get_scores_for_board()

        clear_scores_button = Button(Localization.get_text('clear_scores'))
        #clear_scores_button.set_click(lambda: MainMenuScreen())

        back_button = Button(Localization.get_text('back'))
        back_button.set_click(lambda: GameTypePickerScreen('best_scores', lambda x: ScoresScreen(x)))

        buttons = (clear_scores_button, back_button)

        super().__init__(buttons, f"{Localization.get_text('best_scores')} {self.board_name}", 60)


    def show(self, game):

        return super().show(game)


from Screens.GameTypePickerScreen import GameTypePickerScreen