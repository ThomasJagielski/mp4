"""
This is near replica of Super Mario World 1-1, a classic
in the video gaming world. This project was done in March
2019 for Mini Project 4 in Software Design

authors: awenstrup and ThomasJagielski
"""

#----------Import Statements------------------
import pygame as pg
from pygame.locals import *
pg.init()

#import keyboard as k

#from mario import Mario
#from mushroom import Mushroom
#from decorations import Decorations
from goomba import Goomba

#----------Global Variable Definitions-----------
display_height = 600
display_width = 800

black = (0,0,0)
white = (255,255,255)

#----------Helper Functions-------------
def setup_window():
    screen = pg.display.set_mode((display_width,display_height))
    #screen.set_caption('Mario Level 1-1')
    return screen

#----------Testing Functions--------------
def add_goobma_test():
    g1 = Goomba(0, 0, 0, 0)
    g1_rect = g1.image.get_rect()
#----------Main Method---------------
def main():
    screen = pg.display.set_mode((display_width, display_height))
    g1 = Goomba(0, 0, 0, 0)


    while 1:
        pg.display.update()
        screen.fill(white)
        screen.blit(g1.image, g1.rect)
        pg.display.flip()
        g1.update()
        #if(k.is_pressed('q')):
    #        pg.quit()
    #quit()
    return

main()
