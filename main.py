"""
This is near replica of Super Mario World 1-1, a classic
in the video gaming world. This project was done in March
2019 for Mini Project 4 in Software Design

authors: awenstrup and ThomasJagielski
"""

#----------Import Statements------------------
import pygame
from pygame.locals import *
pygame.init()

#import keyboard as k

#from mario import Mario
#from mushroom import Mushroom
#from decorations import Decorations
from goomba import Goomba
from controller import Controller
from view import View
from mario import Mario
from model import Model
from cloud import Cloud
from bricks import Brick
from air_brick import Air_Bricks
from pipe import Pipe
from flag import Flag
from castle import Castle
import random


#----------Global Variable Definitions-----------
display_height = 600
display_width = 800

black = (0,0,0)
white = (255,255,255)

length = 3000

#----------Helper Functions-------------
def setup_window():
    screen = pygame.display.set_mode((display_width,display_height))
    #screen.set_caption('Mario Level 1-1')
    return screen

#----------Testing Functions--------------
def add_goobma_test():
    g1 = Goomba(0, 0, 0, 0)
    g1_rect = g1.image.get_rect()
#----------Main Method---------------
def main2():
    screen = pygame.display.set_mode((display_width, display_height))
    g1 = Goomba(0, 0, 0, 0)

    '''
    mario = Mario()
    model = Model()
    controller = Controller(model, mario)

    view = View()
    '''

    running = True
    while running:
        '''
        controller.update()
        view.draw()
        '''

        pygame.display.update()
        screen.fill(white)
        screen.blit(g1.image, g1.rect)
        pygame.display.flip()
        g1.update()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
    pygame.quit()

def main():
    mario = Mario(x= 400, y=300)
    model = Model(mario)
    mario.model = model
    model.items.append(Goomba(model, 800, 300, -0.1, 0))
    model.items.append(Goomba(model, 1500, 300, -0.1, 0))
    model.items.append(Goomba(model, 700, 300, -0.1, 0))
    model.items.append(Goomba(model, 2000, 300, -0.1, 0))
    model.items.append(Goomba(model, 1000, 300, -0.1, 0))
    model.items.append(Pipe(model, 800, 425, height = 125))
    model.items.append(Flag(model, length - 275, 250))
    model.items.append(Castle(model, length - 200, 350))
    model.items.append(Air_Bricks(model, 700, 450))
    for n in range(1, length, 400):
        model.items.append(Cloud(x= n, y=random.randint(50, 250)))
    for i in range(1,length,30):
        model.items.append(Brick(x = i, y = 540))
        model.items.append(Brick(x = i, y = 570))
    controller = Controller(model, mario)

    view = View(model)

    running = True
    while running:
        controller.update()
        view.draw()
        controller.key_input()

        if mario.dead:
            pass

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False

    pygame.quit()

main()
