from Side import Side

class Board:
    """
    Class representing board
    """

    def __init__(self, x_, y_, pipes_):
        """
        Constructor
        """
        self.x = x_
        self.y = y_
        self.pipes = pipes_.copy()
        self.start_pipe = pipes_[0]
        self.end_pipe = pipes_[-1]
        self.table = [[0 for x in range(self.x)] for y in range(self.y)]

        for pipe in pipes_:
            self.table[pipe.x][pipe.y] = pipe

        for i in range(self.x):
            for j in range(self.y):
                if self.table[i][j] == 0:
                    raise Exception("Incorrect pipe list initialization")


    def get_coordinates_shifted_by_side(self, x, y, side):
        if side == Side.Left:
            return x - 1, y
        elif side == Side.Up:
            return x, y - 1
        elif side == Side.Right:
            return x + 1, y
        elif side == Side.Down:
            return x, y + 1
    

    def connected_pipes_generator(self, pipe):
        for output in pipe.outputs:
            x, y = self.get_coordinates_shifted_by_side(pipe.x, pipe.y, output.side)
            if x in range(self.x) and y in range(self.y):
                neighbour_pipe = self.table[x][y]
                if output.get_opposite().side in (neighbour_output.side for neighbour_output in neighbour_pipe.outputs):
                    yield neighbour_pipe


    def exists_connection_between_start_and_end_pipes(self):
        checked_pipes = set()
        pipes = list(self.get_all_connected_pipes(self.start_pipe, checked_pipes))
        return self.end_pipe in pipes


    def get_all_connected_pipes(self, pipe, checked_pipes):
        if pipe not in checked_pipes:
            checked_pipes.add(pipe)
            for next_pipe in self.connected_pipes_generator(pipe):
                yield from self.get_all_connected_pipes(next_pipe, checked_pipes)
            yield pipe