from Direction import Direction
from Side import Side

class Pipe:
    """
    Class representing pipe
    """
    
    def __init__(self, outputs_, x_, y_):
        """ 
        Constructor 
        
        init(list, int, int)
        
        outputs_ - list of outputs (type Direction)
        x_ - coordinate x
        y_ - coordinate y
        """
        self.outputs = outputs_.copy()
        self.x = x_
        self.y = y_
        

    def rotate(self, clockwise = True):
        for o in self.outputs:
            o.rotate(clockwise)


    def __repr__(self):
        return f"x: {self.x}, y:{self.y}, outputs: {','.join(str(o) for o in self.outputs)}"
            

    @classmethod
    def get_streight(cls, x, y):
        directions = [Direction(Side.Left), Direction(Side.Right)]
        return Pipe(directions, x, y)
    

    @classmethod
    def get_nodus(cls, x, y):
        directions = [Direction(Side.Left), Direction(Side.Up)]
        return Pipe(directions, x, y)