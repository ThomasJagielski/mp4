import pygame as pg
from items import Items

class Flag(Items):
    def __init__(self, model, x=0, y=0, width = 50, height = 300):
        self.image = pg.image.load('media/Flagpole.png')
        self.width = width
        self.height = height
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.model = model

    def check_win(self):
        if self.model.mario.x > self.x:
            self.model.win = True

    def update(self):
        self.check_win()
