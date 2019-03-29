from items import Items
import pygame as pg
import random

class Pipe(Items):
    def __init__(self, model, x=0, y=0, width = 100, height = 50):
        self.image = pg.image.load('media/pipe.png')
        self.width = width
        self.height = height
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.range = (self.x - 18, self.x - 18 + self.width)
        self.model = model

    def block_mario(self):
        if (not self.rect.colliderect(self.model.mario.rect)):
            self.model.mario.blocked_left = False
            self.model.mario.blocked_right = False
        elif (self.model.mario.x < self.x):
            self.model.mario.blocked_right = True
        elif (self.model.mario.x > self.x):
            self.model.mario.blocked_left = True

    def block_mario_down(self):
        if (self.model.mario.y < self.y and self.rect.colliderect(self.model.mario.rect)):
            self.model.mario.ground = self.model.mario.GROUND - self.height + 15
            self.model.mario.in_air = False
            self.model.mario.vy = 0
            self.model.mario.blocked_left = False
            self.model.mario.blocked_right = False
        else:
            self.model.mario.ground = self.model.mario.GROUND

    def update(self):
        self.block_mario()
        self.block_mario_down()
        self.rect = self.image.get_rect(topleft=((self.x-18, self.y-15)))
