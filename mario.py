from character import Character
import pygame as pg

class Mario(Character):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        """ Iniaitialize mario with a position (x and y) and a change in position (vx and vy)"""
        # initialize the x and y positon of mario
        self.x = x
        self.y = y
        # initialize the change in x and y
        self.vx = vx
        self.vy = vy
        # initialize the model of mario
        self.model = None
        # input the image of mario moving to left and the right
        self.image_right = pg.image.load('media/mario_jumping.png')
        self.image_left =  pg.image.load('media/mario_reverse.png')
        # rescale the images of mario
        self.image_right = pg.transform.scale(self.image_right, (32, 32))
        self.image_left = pg.transform.scale(self.image_left, (32, 32))
        # initialize the image of mario to moving to the right
        self.image = self.image_right
        # define the global of mario's ground
        self.GROUND = 505
        # set mario's ground to the GROUND global
        self.ground = self.GROUND
        # initialize mario's gravity
        self.grav = -0.002
        # intialize in_air global to True
        self.in_air = True
        # intialize mario as not being blocked
        self.blocked_right = False
        self.blocked_left = False
        self.blocked_up = False
        # intialize mario as not being dead
        self.dead = False
        # define the rectangle around the image of mario
        self.rect = self.image.get_rect()
        # initialize mario as moving to the right
        self.moving_right = True

    def move(self):
        """ Definition of cases for mario's movement """
        # if mario is in the air move mario down with the force of gravity until he reaches the ground
        self.vy -= self.grav
        # change the frame of the model based on the change in x
        self.vx = self.model.frame.vx
        # check if mario is blocked in any direction
        if ((self.blocked_left and self.vx < 0) or (self.blocked_right and self.vx > 0)):
            pass
        else:
            # if he is not blocked change the x value based on the change in x
            self.x += self.vx
        # check if mario is block in the upwards direction
        if (self.blocked_up):
            # if blocked do not move upwards
            self.vy = 0
            # move the y position down 2 pixels, so mario is no longer blocked
            self.y += 2
            # reset the blocked_up global to false
            self.blocked_up = False
        else:
            # if mario is not blocked in the upwards direction change mario's position based off the change in y
            self.y += self.vy
        # Check if mario is above the ground
        if (self.y > self.ground):
            # set mario's postion to the height of the ground
            self.y = self.ground
            # do not change the y value when mario is on the ground
            self.vy = 0
            # reset mario's in_air global to false
            self.in_air = False

    def update_image(self):
        """ Update the image based off if mario is moving to the right or to the left """
        # if mario is moving to the right, display the moving to the right image
        if self.vx > 0 & self.moving_right == False:
            self.image = self.image_right
            self.moving_right = True
        # if mario is moving to the left, display the moving to the left 
        elif self.vx < 0 & self.moving_right:
            self.image = self.image_left
            self.moving_right = False

    def update(self):
        """ Update mario and mario's rectangle based on movement input """
        # change the x and y positon of mario
        self.move()
        # change mario's rectangle to match the x and y position
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # change the image based off which direction mario is moving/facing
        self.update_image()
