from items import Items
import pygame as pg
import random

class Pipe(Items):
    def __init__(self):
        self.__init__(self,image ='media/pipes.png')
        self.image = pg.transform.scale(self.image, (100, 50))

