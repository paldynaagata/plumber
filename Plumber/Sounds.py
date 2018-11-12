import pygame
import random
import Settings
import Constants

from Singleton import Singleton

class __Sounds(metaclass = Singleton):
    """
    Class responsible for playing sounds
    """

    def _play(self, path):
        if Settings.get_sound_enable():
            effect = pygame.mixer.Sound(path)
            effect.play()


    def play_pipe_rotate(self):
        sound_index = random.randint(0, len(Constants.click_sounds) - 1)
        self._play(Constants.click_sounds[sound_index])


    def play_button_click(self):
        self._play(Constants.menu_click_sound)


    def play_winning(self):
        self._play(Constants.win_sound)


instance = __Sounds()


def play_pipe_rotate():
    instance.play_pipe_rotate()


def play_button_click():
    instance.play_button_click()


def play_winning():
    instance.play_winning()