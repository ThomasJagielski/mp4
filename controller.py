import pygame as pg

class Controller:
    def __init__(self, model, mario):
        self.model = model
        self.mario = mario

    def key_input(self,key):
        if key.type != pg.locals.KEYDOWN:
            return
        if event.key == pg.K_LEFT:
            self.model.frame.vx = -1.0
        if event.key == pg.K_RIGHT:
            self.model.frame.vx = 1.0
        if event.key == pg.K_UP:
            self.model.mario.vy = -1.0

        # Down for pipes, later

    def update_func(self):
        self.key_input()
        self.model.update()
