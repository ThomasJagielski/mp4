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

        self.grav = -0.002
        self.in_air = True
        #self.image = self.get_image(0,4,16,16)
        #self.image_dead = self.get_image(61, 0, 16, 16)

        self.rect = self.image.get_rect()

    def move(self):
        self.vy -= self.grav
        self.vx = self.model.frame.vx
        self.x += self.vx
        self.y += self.vy

        if (self.y > 505):
            self.y = 505
            self.vy = 0
            self.in_air = False

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        print("Mario: x=", self.x, " y=", self.y)
