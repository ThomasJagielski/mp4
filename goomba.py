from character import Character
import pygame as pg
from pipe import Pipe

class Goomba(Character):

    def __init__(self, model, x=0, y=0, vx=0, vy=0):

        self.model = model

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = pg.image.load('media/goomba.png')
        self.image = pg.transform.scale(self.image, (24, 24))
        #self.image = self.get_image(0,4,16,16)
        #self.image_dead = self.get_image(61, 0, 16, 16)

        self.rect = self.image.get_rect()

        self.grav = -0.002
        self.erase_me = False



    def move(self):
        self.vy -= self.grav
        self.x += self.vx
        self.y += self.vy

        self.rect.x += self.vx
        self.rect.y += self.vy

        if (self.y > 515):
            self.y = 515
            self.vy = 0
            self.in_air = False

    def stepped_on(self):
        self.image_dead = pygame.image.load('')

    def check_mario_collision(self):
        if self.rect.colliderect(self.model.mario.rect):
            if self.model.mario.vy > 0:
                self.model.mario.vy = -0.2
                self.erase_me = True
            else:
                self.model.kill_mario = True

    def check_pipe_collision(self):
        for item in self.model.items:
            if type(item) is Pipe and self.rect.colliderect(item.rect):
                self.vx *= -1

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
        self.rect = self.image.get_rect(center=((self.x, self.y)))
        self.check_mario_collision()
        self.check_pipe_collision()
