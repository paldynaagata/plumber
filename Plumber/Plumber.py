"""
"Plumber"

Author: Agata Paldyna
"""

import pygame

from Pipe import Pipe
from Direction import Direction
from Side import Side


def get_coordinates_shifted_by_side(x, y, side):
    if side == Side.Left:
        return x - 1, y
    elif side == Side.Up:
        return x, y + 1
    elif side == Side.Right:
        return x + 1, y
    elif side == Side.Down:
        return x, y - 1
    
def connected_pipes_generator(table, pipe):
    for output in pipe.outputs:
        x, y = get_coordinates_shifted_by_side(pipe.x, pipe.y, output.side)
        if x in range(len(table)) and y in range(len(table[0])):
            yield table[x][y]
            
            
#outputs1 = [Direction(Side.Left), Direction(Side.Right)]
#pipe1 = Pipe(outputs1, 1, 3)
#for o in pipe1.outputs:
#    print(o.side.name)
#pipe1.rotate(False)
#for o in pipe1.outputs:
#    print(o.side.name)
#    
#dir1 = Direction(Side.Up)
#print(dir1.get_opposite().side.name)

table = [[0 for x in range(3)] for y in range(3)]
for i in range(3):
    for j in range(3):
        if  i == 1 and (j == 0 or j == 2):
            table[i][j] = Pipe.get_nodus(i, j)
        else:
            table[i][j] = Pipe.get_streight(i,j)
            
table[1][1].rotate()
table[1][0].rotate()
table[1][0].rotate()

start_pipe = table[2][0]
end_pipe = table[0][2]

checked_pipes = set((start_pipe))
current_pipe = start_pipe
for pipe in  connected_pipes_generator(table, current_pipe):
    if pipe not in checked_pipes and current_pipe in connected_pipes_generator(table, pipe):
        



#pygame.init()
#window = pygame.display.set_mode((800, 500))
#pygame.display.set_caption("Plumber")
#
#run = True
#
#while run:
#    pygame.time.delay(100)
#    
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            run = False
#
#pygame.quit()