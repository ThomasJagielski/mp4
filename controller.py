import pygame as pg

class Controller:
    def __init__(self, model, mario):
        self.model = model
        self.mario = mario

        self.jump_flag = False
        self.right_flag = False
        self.left_flag = False


    def key_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.left_flag = True
        if keys[pg.K_RIGHT]:
            self.right_flag = True
        if keys[pg.K_UP] and (not self.mario.in_air):
            self.jump_flag = True
        # Down for pipes, later

    def update(self):
        self.model.update()
        self.move_left()
        self.model.update()
        self.move_right()
        self.jump()

    def jump(self):
        if self.jump_flag and (not self.mario.in_air):
            self.mario.vy = -0.75
            self.mario.in_air = True
            self.jump_flag = False
        return

    def move_right(self):
        if self.right_flag == True:
            self.model.frame.vx = 0.5
            self.right_flag = False
        else:
            self.model.frame.vx = 0.0
        return

    def move_left(self):
        if self.left_flag == True:
            self.model.frame.vx = -0.5
            self.left_flag = False
            return
        else:
            self.model.frame.vx = 0.0
