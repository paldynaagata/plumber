from Side import Side

class Direction:
    """
    Class representing direction of pipe's outputs
    """
    
    def __init__(self, side_):
        self.side = side_
    

    def get_opposite(self):
        return Direction(Side((self.side.value + 2) % 4))
    

    def rotate(self, clockwise = True):
        sign = 1 if clockwise else -1
        self.side = Side((self.side.value + sign) % 4)


    def __repr__(self):
        return self.side.name