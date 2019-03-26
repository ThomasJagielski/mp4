from character import Character
import pygame as pg

class Mario(Character):
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.model = None
        self.image = pg.image.load('media/mario_jumping.png')
        self.image = pg.transform.scale(self.image, (32, 32))

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

    def move(self):
        self.vy -= self.grav
        self.vx = self.model.frame.vx
        if ((self.blocked_left and self.vx < 0) or (self.blocked_right and self.vx > 0)):
            pass
        else:
            self.x += self.vx
        self.y += self.vy

        if not self.vx == 0:
            print("Mario x: ", self.x)
            print(self.blocked_left, self.blocked_right)
        if (self.y > self.ground):
            self.y = self.ground
            self.vy = 0
            self.in_air = False

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
        self.rect = self.image.get_rect(center=(self.x, self.y))
