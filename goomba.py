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

        self.grav = -0.002
        self.erase_me = False



    def move(self):
        self.vy -= self.grav
        self.x += self.vx
        self.y += self.vy

        self.rect.x += self.vx
        self.rect.y += self.vy

        if (self.y > 492):
            self.y = 492
            self.vy = 0
            self.in_air = False

    def stepped_on(self):
        self.image_dead = pygame.image.load('')

    def check_mario_collision(self):
        if self.rect.colliderect(self.model.mario.rect):
            if self.model.mario.in_air and self.model.mario.vy > 0:
                self.model.mario.vy = -0.2
                self.erase_me = True
                print('Dead')
            else:
                pass

    def update(self):
        """
        Update the x and y position of the Goomba
        """
        self.move()
        self.rect = self.image.get_rect(center=((self.x, self.y)))
        self.check_mario_collision()
        print("Goomba: x=", self.x, " y=", self.y)
