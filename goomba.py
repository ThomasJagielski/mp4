from character import Character
import pygame as pg

class Goomba(Character):

    def __init__(self, model, x=0, y=0, vx=0, vy=0):

        self.model = model

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = pg.image.load('media/goomba.png')
        self.image = pg.transform.scale(self.image, (60, 60))
        #self.image = self.get_image(0,4,16,16)
        #self.image_dead = self.get_image(61, 0, 16, 16)

        self.rect = self.image.get_rect()

    def move(self):
        self.x += self.vx
        self.y += self.vy

        self.rect.x += self.vx
        self.rect.y += self.vy

    def stepped_on(self):
        self.image_dead

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
