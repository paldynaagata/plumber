from Pipe import Pipe
import pygame

class GamePipe(Pipe):
    """
    Class representing pipe with image of pipe, 
    inherited class Pipe
    """

    def __init__(self, sides_, x_, y_):
        super().__init__(sides_, x_, y_)

        if len(sides_) == 2:
            if self.outputs[0].side == self.outputs[1].get_opposite().side:
                self.image_path = 'Images/pipe_straight.png'
            else:
                self.image_path = 'Images/pipe_nodus.png'
        else:
            raise Exception('There is no image for that')

        self.image = pygame.image.load(self.image_path)


    def rotate(self, clockwise = True):
        super().rotate(clockwise)
        if not self.block_rotate:
            angle = -90 if clockwise else 90
            self.image = pygame.transform.rotate(self.image, angle)