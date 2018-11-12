import pygame
import Localization

from Screens.MenuScreen import MenuScreen
from Screens.ScoresScreen import ScoresScreen
from UIItems.Button import Button

class MainMenuScreen(MenuScreen):
    """
    Class representing main menu screen,
    inherited class Screen
    """

    def __init__(self):
        new_game_button = Button(Localization.get_text('new_game'))
        new_game_button.set_click(lambda: NewGameMenuScreen())

        scores_button = Button(Localization.get_text('scores'))
        scores_button.set_click(lambda: ScoresScreen())

        settings_button = Button(Localization.get_text('settings'))
        settings_button.set_click(lambda: SettingsScreen())

        exit_button = Button(Localization.get_text('exit'))
        exit_button.set_click(lambda: None)

        buttons = (new_game_button, scores_button, settings_button, exit_button)

        super().__init__(buttons, "Plumber", 110)


from Screens.SettingsScreen import SettingsScreen
from Screens.NewGameMenuScreen import NewGameMenuScreen
from Screens.GameScreen import GameScreen
# it is here because modules import each other