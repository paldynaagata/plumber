import pygame

from Screens.GameScreen import GameScreen
from Screens.Screen import Screen

class Game:
    """
    Class representing a game
    """

    def __init__(self):
        pygame.init()
        #self.current_screen = MainMenuScreen()
        self.current_screen = GameScreen()
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Plumber")


    def play_loop(self):
        run = True

        while run:
            pygame.time.delay(100)
            self.window.fill((0,0,0))
            pygame.font.init()
    
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False

            self.current_screen = self.current_screen.show(self.window, events)
            if self.current_screen is None:
                run = False

            pygame.display.update()

        pygame.quit()