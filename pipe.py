from items import Items
import pygame as pg
import random

class Pipe(Items):
    def __init__(self, model, x=0, y=0, width = 100, height = 50):
        # initialize the image of the pipe
        self.image = pg.image.load('media/pipe.png')
        # set the width and height of the pipe
        self.width = width
        self.height = height
        # reshape the image of pipe based on the width and height of the pipe
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        # initialize a rectangle around the scaled image of the pipe
        self.rect = self.image.get_rect()
        # set the pipe's x and y position
        self.x = x
        self.y = y
        # set the range of values of the pipe
        self.range = (self.x - 18, self.x - 18 + self.width)
        # initialize the model for interaction
        self.model = model

    def block_mario(self):
        # check if there is a collision between the pipe and mario
        if (not self.rect.colliderect(self.model.mario.rect)):
            # if there is no collision set blocked_left and blocked_right to false
            self.model.mario.blocked_left = False
            self.model.mario.blocked_right = False
        elif (self.model.mario.x < self.x):
            # if there is a collision and mario's x value is less than the pipe's, mario is blocked on the right
            self.model.mario.blocked_right = True
        elif (self.model.mario.x > self.x):
            # if there is a collision and mario's x value is greater than the pipe's, mario is blocked on the left
            self.model.mario.blocked_left = True

    def block_mario_down(self):
        # check if there is a collision between mario and the pipe
        if (self.model.mario.y < self.y and self.rect.colliderect(self.model.mario.rect)):
            # redefine the ground as being on top of the pipe if there is a collision and mario's y value is greater than the pipe's
            self.model.mario.ground = self.model.mario.GROUND - self.height + 15
            # reset mario's in_air flag to false
            self.model.mario.in_air = False
            # set mario's change in y to zero
            self.model.mario.vy = 0
            # set mario to not be blocked on the left or the right
            self.model.mario.blocked_left = False
            self.model.mario.blocked_right = False
        else:
            # otherwise, reset mario's ground to the initial position of ground (505)
            self.model.mario.ground = self.model.mario.GROUND

    def update(self):
        # check is mario is blocked left or right
        self.block_mario()
        # check if mario is on top of the pipe
        self.block_mario_down()
        # change the position of the pipe depending on the change in x and y
        self.rect = self.image.get_rect(topleft=((self.x-18, self.y-15)))
