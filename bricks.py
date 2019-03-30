import pygame as pg

class Brick():
    def __init__(self, x = 0, y = 0):
        """ Initialize the ground bricks with an x and y position """
        # initialize the x and y position of the block
        self.x = x
        self.y = y
        # load the images of the block, resize it, and form a rectangle around it
        self.image = pg.image.load('media/ground_brick.png')
        self.image = pg.transform.scale(self.image, (30, 30))

    def update(self):
        # Update - but nothing is changing as it is a decoration
        pass
