import pygame
import Localization

from pygame import Rect
from Scores import Scores
from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText
from Screens.ScoresScreen import ScoresScreen

class GameSummaryScreen(MenuScreen):
    """
    Class representing summary of the game screen,
    inherited class MenuScreen
    """

    def __init__(self, click_count, board_size):
        self.click_count = click_count
        self.board_size = board_size
        self.user_name = ""
        self.board_name = f"{self.board_size}x{self.board_size}"

        self.scores = Scores(self.board_name)
        self.show_input = self.scores.is_score_rated(self.click_count)

        menu_button = Button(Localization.get_text('menu'))
        menu_button.set_click(lambda: MainMenuScreen())

        buttons = [menu_button]

        super().__init__(buttons, Localization.get_text('congratulations'), 60)


    def show(self, game):
        text_ = str.format("{0} {1}.", Localization.get_text('score'), self.click_count)
        text = CenteredText(text_, 40, (0, 0, 0))
        text.write(game.window, y = game.window.get_height() / 2 - 4 * text.size)

        if self.show_input:
            text = CenteredText(Localization.get_text('enter_name'), 20, (0, 0, 0))
            text.write(game.window, y = game.window.get_height() / 2 - 2 * text.size)

            rect_width = 300
            rect_height = 50
            rect = Rect(((game.window.get_width() - rect_width) / 2, (game.window.get_height() + 1.5 * rect_height) / 2), (rect_width, rect_height))
            pygame.draw.rect(game.window, (255, 255, 255), rect)

            user_name_text = CenteredText(self.user_name, 20, (0, 0, 0))
            user_name_text.write(game.window, rect)

            for event in game.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.user_name) > 0:
                            self.scores.add_score(self.user_name, self.click_count)
                            return ScoresScreen(self.board_name)
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_name = self.user_name[:-1]
                    elif event.key != pygame.K_COMMA and len(self.user_name) <= 16:
                        self.user_name += event.unicode

        return super().show(game)


from Screens.MainMenuScreen import MainMenuScreen