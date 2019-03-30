from decorations import Decorations
import pygame as pg

class Castle(Decorations):
    def __init__(self, model, x=0, y=0, width = 200, height = 200):
        """ Initialize the castle decoration with a reference to the model,
        a x and y position, and a size defined by width and height """
        # load the image of the castle
        self.image = pg.image.load('media/castle.png')
        # set the size of the castle
        self.width = width
        self.height = height
        # resize the castle based on the width and height of the image
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        # define a new rectangle around the image
        self.rect = self.image.get_rect()
        # set the x and y positions
        self.x = x
        self.y = y
        self.model = model
