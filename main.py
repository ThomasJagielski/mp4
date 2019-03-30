"""
This is near replica of Super Mario World 1-1, a classic
in the video gaming world. This project was done in March
2019 for Mini Project 4 in Software Design

authors: awenstrup and ThomasJagielski
"""

#----------Import Statements------------------
import pygame
from pygame.locals import *
# intialize pygame
pygame.init()

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
# define the display window size
display_height = 600
display_width = 800

# define the length of the world
length = 3000

# create a mario with an initial position of x = 400 and y = 300
mario = Mario(x= 400, y=300)
# create a model with mario 
model = Model(mario)
# set mario's model to the model created
mario.model = model

# intialize the controller
controller = Controller(model, mario)
# intialize the view
view = View(model)

#----------Helper Functions-------------
def setup_window():
    # intialize the game window
    screen = pygame.display.set_mode((display_width,display_height))
    screen.set_caption('Mario Level 1-1 Parody')
    return screen

#----------Add Items--------------
def add_ground():
    """
    Add the ground image
    """
    for i in range(1,length,30):
        model.items.append(Brick(x = i, y = 540))
        model.items.append(Brick(x = i, y = 570))  

def add_items():
    # create all instances of goombas
    model.items.append(Goomba(model, 700, 300, -0.1, 0))
    model.items.append(Goomba(model, 800, 300, -0.1, 0))
    model.items.append(Goomba(model, 1000, 300, -0.1, 0))
    model.items.append(Goomba(model, 1300, 300, -0.1, 0))
    model.items.append(Goomba(model, 1500, 300, -0.1, 0))
    model.items.append(Goomba(model, 1700, 300, -0.1, 0))
    model.items.append(Goomba(model, 2800, 300, -0.1, 0))
    model.items.append(Goomba(model, 3000, 300, -0.1, 0))
    # create all instances of pipes
    model.items.append(Pipe(model, 800, 425, height = 125))
    model.items.append(Pipe(model, 2000, 425, height = 125))
    # create all instances of bricks in the air
    model.items.append(Air_Bricks(model, 550, 450))
    model.items.append(Air_Bricks(model, 1000, 450))
    model.items.append(Air_Bricks(model, 1400, 450))
    model.items.append(Air_Bricks(model, 2600, 450))
    # create the flag and castle
    model.items.append(Flag(model, length - 275, 250))
    model.items.append(Castle(model, length - 200, 350))
    # add clouds to display
    for n in range(1, length, 400):
        model.items.append(Cloud(x= n, y=random.randint(50, 250))) 
    
#----------Main Method---------------
def main():
    # add all the items
    add_items()
    # add the ground image
    add_ground()
    # update the controller and view when the game is "running"
    running = True
    while running:
        # update the status of the controller
        controller.update()
        # change the view based on the model's view
        view.draw()
        # check for controller input
        controller.key_input()
        # if the quit key is pressed end the game
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
    pygame.quit()

main()
