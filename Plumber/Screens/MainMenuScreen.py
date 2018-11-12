import pygame

from Screens.MenuScreen import MenuScreen
from Screens.ScoresScreen import ScoresScreen
from UIItems.Button import Button

class MainMenuScreen(MenuScreen):
    """
    Class representing main menu screen,
    inherited class Screen
    """

    def __init__(self):
        new_game_button = Button("New Game")
        new_game_button.set_click(lambda: NewGameMenuScreen())

        scores_button = Button("Scores")
        scores_button.set_click(lambda: ScoresScreen())

        settings_button = Button("Settings")
        #settings_button.set_click(lambda: SettingsScreen())

        exit_button = Button("Exit")
        exit_button.set_click(lambda: None)

        buttons = (new_game_button, scores_button, settings_button, exit_button)

        super().__init__(buttons, "Plumber", 110)

from Screens.NewGameMenuScreen import NewGameMenuScreen
from Screens.GameScreen import GameScreen
# it is here because modules import each other