#from items import Item
import pygame as pg

class Air_Bricks():
    def __init__(self, model, x = 0, y = 0):
        # set the x and y poisition of the block
        self.x = x
        self.y = y
        # initialize the model for interactions
        self.model = model
        # load the image of bricks in the air
        self.image = pg.image.load('media/brick_air.png')
        # scale the image and create a rectange for it
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

    def block_mario(self):
        if (self.rect.colliderect(self.model.mario.rect)):
            # if mario is on top of the air bricks
            if (self.model.mario.y > self.y):
                if self.model.mario.x - self.x < -25: #blocked on the right
                    # set flags to show mario is blocked on the right
                    self.model.mario.blocked_left = False
                    self.model.mario.blocked_right = True
                elif self.model.mario.x - self.x > 20: #blocked on the left
                    # set flags to show mario is blocked on the left
                    self.model.mario.blocked_right = False
                    self.model.mario.blocked_left = True
                elif self.model.mario.vy < 0: # redefine mario's ground if he is on top of the air bricks
                    self.model.mario.ground = self.model.mario.GROUND
                    self.model.mario.blocked_up = True
            else:
                if self.model.mario.x - self.x < -25: #blocked on the right
                    # set flags to show mario is blocked on the right
                    self.model.mario.blocked_left = False
                    self.model.mario.blocked_right = True
                elif self.model.mario.x - self.x > 20: #blocked on the left
                    # set flags to show mario is blocked on the left
                    self.model.mario.blocked_right = False
                    self.model.mario.blocked_left = True
                else: #blocked from the bottom
                    self.model.mario.ground = self.y - 30
                    self.model.mario.blocked_up = False

    def update(self):
        # update the status of the model to show if mario is interacting with the blocks, and thus, is blocked in some direction
        self.block_mario()
        self.rect = self.image.get_rect(topleft=((self.x - 15, self.y - 17)))
