from decorations import Decorations
import pygame as pg

class Cloud(Decorations):
    def __init__(self, x=0, y=0):
        """ Initialize the cloud decorations with a x and y postion """
        # set the x and y position of the clouds
        self.x = x
        self.y = y
        # load the image of a cloud, scale the image, and define a rectangle around the scaled image
        self.image = pg.image.load('media/cloud.png')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()