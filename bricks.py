#from items import Item
import pygame as pg

class Brick():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.image = pg.image.load('media/ground_brick.png')
        self.image = pg.transform.scale(self.image, (30, 30))

    def ground(self):
        # length of screen (total/25)
        blocks = []
        for i in range(100):
            self.x = i * 50
            blocks.append(self)
        return blocks

