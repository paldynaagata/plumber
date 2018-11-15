import pygame
import math
import Sounds
import Settings
import Localization

from Board import Board
from Screens.MenuScreen import MenuScreen
from PipesImporter import PipesImporter
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText

class GameScreen(MenuScreen):
    """
    Class representing game screen,
    inherited class MenuScreen
    """

    def __init__(self, board_name):
        self.pipes = list()
        self.success = False
        self.board = None
        self._scale_factor = Settings.get_scale_factor()
        self.scale = int(100 * self._scale_factor)
        self.click_count = 0
        self.text = CenteredText('', 40 * self._scale_factor, (255, 153, 153))

        pipes_file_path = f"Boards/{board_name}.txt"
        
        pipes_importer = PipesImporter('GamePipe.GamePipe')
        self.pipes = pipes_importer.get_pipes_from_file(pipes_file_path)
        self.size = int(math.sqrt(len(self.pipes)))
        self.board = Board(self.size, self.size, self.pipes)

        for pipe in self.pipes:
            pipe.image = pygame.transform.scale(pipe.image, (self.scale, self.scale))

        back_button = Button(Localization.get_text('back'))
        back_button.click_method = lambda: GameTypePickerScreen('choose_size', lambda x: GameScreen(x))
        buttons = [back_button]
        super().__init__(buttons, None)


    def _get_frame_rectangle(self, board_x, board_y):
        thickness = 10
        left = board_x - thickness
        top = board_y - thickness
        width = self.board.x * self.scale + 2 * thickness
        height = self.board.y * self.scale + 2 * thickness
        return left, top, width, height


    def show(self, game):
        if self.success:
            return GameSummaryScreen(self.click_count, self.size)

        board_x = (game.window.get_width() - self.scale * self.board.x) // 2
        board_y = (game.window.get_height() - self.scale * self.board.y) // 2
        
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONUP:
                if game.left_mouse_button_clicked or game.right_mouse_button_clicked:
                    clockwise = game.left_mouse_button_clicked

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    pipe_x = (mouse_x - board_x) // self.scale 
                    pipe_y = (mouse_y - board_y) // self.scale

                    if pipe_x in range(self.board.x) and pipe_y in range(self.board.y):
                        self.board.table[pipe_x][pipe_y].rotate(clockwise)
                        self.success = self.board.exists_connection_between_start_and_end_pipes()
                        self.click_count += 1
                        Sounds.play_pipe_rotate()

        pygame.draw.rect(game.window, (51, 26, 0), self._get_frame_rectangle(board_x, board_y))
        pygame.draw.rect(game.window, (0, 0, 0), (board_x, board_y, self.board.x * self.scale, self.board.y * self.scale))

        for pipe in self.pipes:
            game.window.blit(pipe.image, (board_x + self.scale * pipe.x, board_y + self.scale * pipe.y))

        self.text.set_text(f"{Localization.get_text('score')} {self.click_count}.")
        self.text.write(game.window, y = (board_y - self.text.size) / 2)

        if self.success:
            Sounds.play_winning()

        return super().show(game)


from Screens.GameSummaryScreen import GameSummaryScreen
from Screens.GameTypePickerScreen import GameTypePickerScreen
# it is here because modules import each other