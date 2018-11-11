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
        self.left_mouse_button_clicked = False
        self.right_mouse_button_clicked = False

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
    

    def set_mouse_clicked_buttons(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        self.left_mouse_button_clicked = m1 == 1
        self.right_mouse_button_clicked = m3 == 1

    def show(self, window, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.set_mouse_clicked_buttons()

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.left_mouse_button_clicked or self.right_mouse_button_clicked:
                    if self.left_mouse_button_clicked:
                        clockwise = True
                    elif self.right_mouse_button_clicked:
                        clockwise = False

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    pipe_x = mouse_x // self.scale
                    pipe_y = mouse_y // self.scale

                    if pipe_x in range(self.board.x) and pipe_y in range(self.board.y):
                        self.board.table[pipe_x][pipe_y].rotate(clockwise)
                        self.success = self.board.exists_connection_between_start_and_end_pipes()

                    self.left_mouse_button_clicked = False
                    self.right_mouse_button_clicked = False

        for pipe in self.pipes:
            window.blit(pipe.image, (self.scale * pipe.x, self.scale * pipe.y))

        if self.success:
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Brawo!', False, (255, 255, 255))
            window.blit(textsurface, (window.get_width()/2, window.get_height()/2))

        return super().show(window, events)