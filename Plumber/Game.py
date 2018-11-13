import os
import pygame
import platform
import ctypes
import Settings

from Screens.MainMenuScreen import MainMenuScreen
from Screens.Screen import Screen

class Game:
    """
    Class representing a game
    """

    def __init__(self):
        pygame.init()
        if platform.system() == 'Windows':
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()
            width = user32.GetSystemMetrics(0)
            height = user32.GetSystemMetrics(1)
        else:
            display_info = pygame.display.Info()
            width = display_info.current_w
            height = display_info.current_h

        Settings.set_scale_factor(height / 1000)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,50"
        self.events = None
        self.left_mouse_button_clicked = False
        self.right_mouse_button_clicked = False
        self.current_screen = MainMenuScreen()
        self.window = pygame.display.set_mode((width, height - 50))#, pygame.FULLSCREEN)
        pygame.display.set_caption("Plumber")


    def set_mouse_clicked_buttons(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        self.left_mouse_button_clicked = m1 == 1
        self.right_mouse_button_clicked = m3 == 1


    def play_loop(self):
        run = True

        while run:
            pygame.time.delay(20)
            self.window.fill((84, 71, 53))
            pygame.font.init()
    
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.set_mouse_clicked_buttons()

            self.current_screen = self.current_screen.show(self)
            if self.current_screen is None:
                run = False

            if pygame.MOUSEBUTTONUP in self.events:
                self.left_mouse_button_clicked = False
                self.right_mouse_button_clicked = False

            pygame.display.update()

        pygame.quit()
