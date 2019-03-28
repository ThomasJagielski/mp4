from decorations import Decorations
import pygame as pg

class Castle(Decorations):
    def __init__(self, model, x=0, y=0, width = 200, height = 200):
        self.image = pg.image.load('media/castle.png')
        self.width = width
        self.height = height
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.model = model
