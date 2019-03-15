from decorations import Decorations
import pygame as pg

class Cloud(Decorations):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = pg.image.load('media/cloud.png')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()