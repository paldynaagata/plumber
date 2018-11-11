from Direction import Direction
from Side import Side

class Pipe:
    """
    Class representing pipe
    """
    
    def __init__(self, sides_, x_, y_):
        """ 
        Constructor 
        
        init(list, int, int)
        
        sides_ - list of sides of outputs (type Side)
        x_ - coordinate x
        y_ - coordinate y
        """
        self.outputs = [Direction(side) for side in sides_]
        self.x = x_
        self.y = y_
        self.block_rotate = False
        

    def rotate(self, clockwise = True):
        if not self.block_rotate:
            for o in self.outputs:
                o.rotate(clockwise)


    def __repr__(self):
        return f"x: {self.x}, y:{self.y}, outputs: {','.join(str(o) for o in self.outputs)}"
            

    #@classmethod
    #def get_streight(cls, x, y):
    #    directions = [Direction(Side.Left), Direction(Side.Right)]
    #    return Pipe(directions, x, y)
    

    #@classmethod
    #def get_nodus(cls, x, y):
    #    directions = [Direction(Side.Left), Direction(Side.Up)]
    #    return Pipe(directions, x, y)