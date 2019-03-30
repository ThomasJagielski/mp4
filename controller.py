import pygame as pg

class Controller:
    def __init__(self, model, mario):
        """ Initialize the controller with a reference to the model and a mario"""
        # initialize the model and mario contained in the controller class
        self.model = model
        self.mario = mario

        # set all globals to false
        self.jump_flag = False
        self.right_flag = False
        self.left_flag = False


    def key_input(self):
        """ Check for keys being pressed to change the postion of mario"""
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            # if left key was pressed, change global to signify that
            self.left_flag = True
        if keys[pg.K_RIGHT]:
            # if right key was pressed, change global to signify that
            self.right_flag = True
        if keys[pg.K_UP] and (not self.mario.in_air):
            # set the jumping global is mario is not in the air and the up key is pressed
            self.jump_flag = True

    def jump(self):
        """ Definition for mario jumping """
        if self.jump_flag and (not self.mario.in_air):
            # jump with an upwards velocity of 0.75 - gravity (negative is the upwards direction)
            self.mario.vy = -0.75
            # set mario's global of being in the air (to avoid double jumping)
            self.mario.in_air = True
            # reset the jumping flag to false
            self.jump_flag = False

    def move_right(self):
        """ Definition of mario moving to the right """
        if self.right_flag == True and self.mario.blocked_right == False:
            # move to the right with a velocity of 0.5
            self.model.frame.vx = 0.5
            # reset the right_flag global
            self.right_flag = False
            # set mario's moving_right global
            self.mario.moving_right = True
        else:
            # do not change the horizontal position if the right flag is false or mario is blocked
            self.model.frame.vx = 0.0

    def move_left(self):
        """ Definition of mario moving to the left"""
        if self.left_flag == True and self.mario.blocked_left == False:
            # move to the left with a velocity of 0.5
            self.model.frame.vx = -0.5
            # reset the left_flag global
            self.left_flag = False
            # set mario's moving_right global to false
            self.mario.moving_right = False
        else:
            # do not change the horizontal position if the left flag is false or mario is blocked
            self.model.frame.vx = 0.0

    def update(self):
        """ Update the positon of mario based on key inputs """
        # update the model
        self.model.update()
        # check if the left key is pressed and mario should move to the left
        self.move_left()
        # update the model accordingly
        self.model.update()
        # check if the right key is pressed and mario should move to the right
        self.move_right()
        # check if the up key is pressed and mario should jump
        self.jump()