import random
import math

from PipeFactory import PipeFactory
from Side import Side

class PipesImporter:
    """
    Class responsible for importing pipe list from a file
    """

    def __init__(self, pipe_class_name):
        self.factory = PipeFactory(pipe_class_name)
        self.string_to_pipe_getters = [lambda x, y: self.factory.get_pipe((Side.Left, Side.Right), x, y), 
                                       lambda x, y: self.factory.get_pipe((Side.Left, Side.Up), x, y)]


    def _get_file_max_index(self, file):
        current_position = file.tell()
        file.seek(0)
        for i, l in enumerate(file):
            pass
        file.seek(current_position)
        return i


    def get_pipes_from_file(self, file_path):
        with open(file_path, 'r') as file:
            line_index = random.randint(0, self._get_file_max_index(file))
            line = file.readlines()[line_index]
            pipes_data = line.split(" ")
            board_side_len = math.sqrt(len(pipes_data))

            pipes = list()
            x = 0
            y = 0
            for pipe_data in pipes_data:
                getter_index = int(pipe_data[:2], 2)
                pipe = self.string_to_pipe_getters[getter_index](x, y)
                
                rotate_number = int(pipe_data[2:], 2)
                for i in range(rotate_number):
                    pipe.rotate()

                pipes.append(pipe)

                x += 1
                if x >= board_side_len:
                    y += 1
                    x = 0

            return pipes