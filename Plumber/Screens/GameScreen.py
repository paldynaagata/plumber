import pygame
import Sounds

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
        self.click_count = 0

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


    def _get_frame_rectangle(self, board_x, board_y):
        thickness = 10
        left = board_x - thickness
        top = board_y - thickness
        width = self.board.x * self.scale + 2 * thickness
        height = self.board.y * self.scale + 2 * thickness
        return left, top, width, height


    def show(self, game):
        board_x = (game.window.get_width() - self.scale * self.board.x) // 2
        board_y = (game.window.get_height() - self.scale * self.board.y) // 2
        
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONUP:
                if game.left_mouse_button_clicked or game.right_mouse_button_clicked:
                    clockwise = game.left_mouse_button_clicked
                    self.click_count += 1
                    Sounds.play_pipe_rotate()

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    pipe_x = (mouse_x - board_x) // self.scale 
                    pipe_y = (mouse_y - board_y) // self.scale

                    if pipe_x in range(self.board.x) and pipe_y in range(self.board.y):
                        self.board.table[pipe_x][pipe_y].rotate(clockwise)
                        self.success = self.board.exists_connection_between_start_and_end_pipes()

        pygame.draw.rect(game.window, (51, 26, 0), self._get_frame_rectangle(board_x, board_y))
        pygame.draw.rect(game.window, (0, 0, 0), (board_x, board_y, self.board.x * self.scale, self.board.y * self.scale))

        for pipe in self.pipes:
            game.window.blit(pipe.image, (board_x + self.scale * pipe.x, board_y + self.scale * pipe.y))

        if self.success:
            #pygame.time.delay(2000)
            Sounds.play_winning()
            #return GameSummaryScreen(self.click_count, self.time)
            return GameSummaryScreen(self.click_count)

        return super().show(game)

from Screens.GameSumaryScreen import GameSummaryScreen