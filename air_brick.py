#from items import Item
import pygame as pg

class Air_Bricks():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.image = pg.image.load('media/brick_air.png')
        self.image = pg.transform.scale(self.image, (30, 30))

    def update(self):
        pass