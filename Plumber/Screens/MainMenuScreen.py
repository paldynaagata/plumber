import pygame
import Localization

from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button

class MainMenuScreen(MenuScreen):
    """
    Class representing main menu screen,
    inherited class Screen
    """

    def __init__(self):
        new_game_button = Button(Localization.get_text('new_game'))
        new_game_button.click_method = lambda: GameTypePickerScreen('choose_size', lambda x: GameScreen(x))

        scores_button = Button(Localization.get_text('best_scores'))
        scores_button.click_method = lambda: GameTypePickerScreen('best_scores', lambda x: ScoresScreen(x))

        settings_button = Button(Localization.get_text('settings'))
        settings_button.click_method = lambda: SettingsScreen()

        exit_button = Button(Localization.get_text('exit'))
        exit_button.click_method = lambda: None

        buttons = (new_game_button, scores_button, settings_button, exit_button)

        super().__init__(buttons, "Plumber", 110)


from Screens.ScoresScreen import ScoresScreen
from Screens.SettingsScreen import SettingsScreen
from Screens.GameTypePickerScreen import GameTypePickerScreen
from Screens.GameScreen import GameScreen
# it is here because modules import each other