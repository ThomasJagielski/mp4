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

import random


#----------Global Variable Definitions-----------
display_height = 600
display_width = 800

black = (0,0,0)
white = (255,255,255)

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

    mario = Mario(y=300)
    model = Model(mario)
    model.items.append(Goomba(model, 400, 300, 0, 0))
    controller = Controller(model, mario)

    view = View(model)

    running = True
    while running:
        print(model.frame.vx)
        controller.update()
        view.draw()
        controller.key_input()

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False

    pygame.quit()


main()
