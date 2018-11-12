import pygame
import Settings
import Localization

from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText

class SettingsScreen(MenuScreen):
    """
    Class representing settings screen,
    inherited class MenuScreen
    """

    def __init__(self):
        language_button = Button(f"{Localization.get_text('language')}: {Settings.get_language()}")
        language_button.set_click(lambda: (Settings.set_to_next_language(), SettingsScreen())[1])

        sounds_button = Button(f"{Localization.get_text('sounds')}: {Localization.get_text(Settings.get_sound_enable())}")
        sounds_button.set_click(lambda: (Settings.toggle_sound_enable(), SettingsScreen())[1])

        back_button = Button(Localization.get_text('back'))
        back_button.set_click(lambda: MainMenuScreen())

        buttons = (language_button, sounds_button, back_button)

        super().__init__(buttons, Localization.get_text('settings'), 60)
    

    def show(self, game):

        return super().show(game)


from Screens.MainMenuScreen import MainMenuScreen
# it is here because modules import each other