from character import Character
import pygame as pg

class Goomba(Character):

    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = pg.image.load('media/graphics/goomba.jpg')
        #self.image = self.get_image(0,4,16,16)
        #self.image_dead = self.get_image(61, 0, 16, 16)

        self.rect = self.image.get_rect()

    # Code taken from https://github.com/justinmeister/Mario-Level-1/blob/master/data/components/enemies.py lines 46-58
    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))


        image = pg.transform.scale(image, (1, 1))
        return image

    def move(self):
        self.vx = 0
        self.vy = 0
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
