from character import Character
import pygame as pg
from pipe import Pipe

class Goomba(Character):

    def __init__(self, model, x=0, y=0, vx=0, vy=0):
        """ Initialize the goomba with a reference to the model, a position (defined by x and y),
        and a change in the x and y values """
        # intialize the model for interaction
        self.model = model
        # initialize the x and y position of the goomba
        self.x = x
        self.y = y
        # initialize the change in x and y for the goomba
        self.vx = vx
        self.vy = vy
        # load the image of the goomba and rescale it
        self.image = pg.image.load('media/goomba.png')
        self.image = pg.transform.scale(self.image, (24, 24))
        # define a rectangle around the scaled image
        self.rect = self.image.get_rect()
        # set gravity for the goomba
        self.grav = -0.002
        # initialize the erase_me global to false (used for when mario jumps on top of the goomba)
        self.erase_me = False

    def move(self):
        """ Definiton of moving the goomba based on the change in x and y """
        # move the goomba down with the velocity of gravity (negative is upward in a pygame window)
        self.vy -= self.grav
        # move the x and y position of the goomba based off the change in x and y
        self.x += self.vx
        self.y += self.vy
        # move the rectangle at the same rate the goomba image is moving
        self.rect.x += self.vx
        self.rect.y += self.vy
        # set the ground level, if the goomba is on the ground, do not move downwards more
        if (self.y > 515):
            self.y = 515
            self.vy = 0
            self.in_air = False

    def check_mario_collision(self):
        """ Definition of cases for collisions between mario and the goomba """
        # check if mario is colliding with the goomba (based on rectangle intersection)
        if self.rect.colliderect(self.model.mario.rect):
            # if mario is moving downwards or is above the goomba, erase the goomba
            if self.model.mario.vy > 0 or self.y - self.model.mario.y > 15:
                self.model.mario.vy = -0.2
                self.erase_me = True
            else:
                # if mario runs into the goomba end game as mario is "dead"
                self.model.kill_mario = True
                

    def check_pipe_collision(self):
        # check if there is a collision between the goomba and a pipe
        for item in self.model.items:
            if type(item) is Pipe and self.rect.colliderect(item.rect):
                # if there is a collision reverse the direction of the goomba
                self.vx *= -1

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        # update the position of the goomba image
        self.move()
        # update the rectangle accordingly
        self.rect = self.image.get_rect(center=((self.x, self.y)))
        # check for collision between goomba and mario
        self.check_mario_collision()
        # check for collision between goomba and pipe
        self.check_pipe_collision()
