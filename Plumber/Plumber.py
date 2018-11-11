"""
"Plumber"

Author: Agata Paldyna
"""

import pygame

from Board import Board
from Pipe import Pipe

            
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

x = 3
y = 3
pipes = list()

#for i in range(x):
#    for j in range(y):
#        if  j == 1 and (i == 0 or i == 2):
#            table[i][j] = pipe.get_nodus(i, j)
#        else:
#            table[i][j] = pipe.get_streight(i, j)

for i in range(x):
    for j in range(y):
        if  i == 1 and (j == 0 or j == 2):
            pipes.append(Pipe.get_nodus(i, j))
        else:
            pipes.append(Pipe.get_streight(i, j))
            
board = Board(x, y, pipes)

board.table[1][1].rotate()

board.table[1][0].rotate()
board.table[1][0].rotate()
board.table[1][0].rotate()

board.table[1][2].rotate()

zmienna = board.exists_connection_between_start_and_end_pipes()
print(zmienna)


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