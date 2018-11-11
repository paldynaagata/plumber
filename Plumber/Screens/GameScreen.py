import pygame

from Board import Board
from PipeFactory import PipeFactory
from Screens.Screen import Screen
from Side import Side

class GameScreen(Screen):
    """
    Class representing game screen,
    inherited class Screen
    """

    def __init__(self):
        self.pipes = list()
        self.success = False
        self.board = None
        self.scale = 100

        x = 3
        y = 3

        pipe_factory = PipeFactory('GamePipe.GamePipe')

        for i in range(x):
            for j in range(y):
                if  i == 1 and (j == 0 or j == 2):
                    self.pipes.append(pipe_factory.get_pipe((Side.Left, Side.Up), i, j))
                else:
                    self.pipes.append(pipe_factory.get_pipe((Side.Left, Side.Right), i, j))
            
        self.board = Board(x, y, self.pipes)

        for pipe in self.pipes:
            pipe.image = pygame.transform.scale(pipe.image, (self.scale, self.scale))


    def show(self, game):
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONUP:
                if game.left_mouse_button_clicked or game.right_mouse_button_clicked:
                    clockwise = game.left_mouse_button_clicked

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    pipe_x = mouse_x // self.scale
                    pipe_y = mouse_y // self.scale

                    if pipe_x in range(self.board.x) and pipe_y in range(self.board.y):
                        self.board.table[pipe_x][pipe_y].rotate(clockwise)
                        self.success = self.board.exists_connection_between_start_and_end_pipes()

        pygame.draw.rect(game.window, (0, 0, 0), (0, 0, self.board.x * self.scale, self.board.y * self.scale))

        for pipe in self.pipes:
            game.window.blit(pipe.image, (self.scale * pipe.x, self.scale * pipe.y))

        if self.success:
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Brawo!', False, (255, 255, 255))
            game.window.blit(textsurface, (game.window.get_width() / 2, game.window.get_height() / 2))

        return super().show(game)