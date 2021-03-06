import pygame as pg
from items import Items

class Flag(Items):
    def __init__(self, model, x=0, y=0, width = 50, height = 300):
        """ Initialize the flag with a reference to the model, x and y position, 
        and height and width for scaling the image"""
        # load the image of the flag
        self.image = pg.image.load('media/Flagpole.png')
        # set the height and width of the image
        self.width = width
        self.height = height
        # scale the image to the input width and height
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        # define a rectangle around the scaled image
        self.rect = self.image.get_rect()
        # set the x and y position of the flag decoration
        self.x = x
        self.y = y
        # set the model of the class for interations
        self.model = model

    def check_win(self):
        """ Check if mario has passed the flag, and thus, has won"""
        # if the x position of mario is greater than the flagpole set the win global in mario to true
        if self.model.mario.x > self.x:
            self.model.win = True

    def update(self):
        """ Check of mario has won and update the model accordingly """
        # check if mario has won
        self.check_win()
