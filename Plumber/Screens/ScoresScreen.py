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
        scores = Scores(board_name)
        self.scores = scores._get_scores_for_board()

        clear_scores_button = Button(Localization.get_text('clear_scores'))
        clear_scores_button.set_click(lambda: (scores.clear_scores(), ScoresScreen(self.board_name))[1])

        back_button = Button(Localization.get_text('back'))
        back_button.set_click(lambda: GameTypePickerScreen('best_scores', lambda x: ScoresScreen(x)))

        buttons = (clear_scores_button, back_button)

        super().__init__(buttons, f"{Localization.get_text('best_scores')} {self.board_name}", 60)


    def show(self, game):
        i = -2.5
        for score in self.scores:
            text = CenteredText(str.format("{0:<20}                 {1:>10}", score[0], score[1]), 20, (0, 0, 0))
            text.write(game.window, y = game.window.get_height() / 3 + i * text.size)
            i += 2

        return super().show(game)


from Screens.GameTypePickerScreen import GameTypePickerScreen