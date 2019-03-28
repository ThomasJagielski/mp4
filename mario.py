from character import Character
import pygame as pg

class Mario(Character):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.model = None
        self.image_right = pg.image.load('media/mario_jumping.png')
        self.image_left =  pg.image.load('media/mario_reverse.png')
        self.image_right = pg.transform.scale(self.image_right, (32, 32))
        self.image_left = pg.transform.scale(self.image_left, (32, 32))
        self.image = self.image_right

        self.GROUND = 505
        self.ground = self.GROUND
        self.grav = -0.002
        self.in_air = True
        self.blocked_right = False
        self.blocked_left = False

        self.dead = False
        #self.image = self.get_image(0,4,16,16)
        #self.image_dead = self.get_image(61, 0, 16, 16)

        self.rect = self.image.get_rect()
        self.moving_right = True

    def move(self):
        self.vy -= self.grav
        self.vx = self.model.frame.vx
        if ((self.blocked_left and self.vx < 0) or (self.blocked_right and self.vx > 0)):
            pass
        else:
            self.x += self.vx
        self.y += self.vy

        if (self.y > self.ground):
            self.y = self.ground
            self.vy = 0
            self.in_air = False

    def update_image(self):
        if self.vx > 0 & self.moving_right == False:
            self.image = self.image_right
            self.moving_right = True
        elif self.vx < 0 & self.moving_right:
            self.image = self.image_left
            self.moving_right = False

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.update_image()
