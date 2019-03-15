"""
Code adapted from example showed in class with the brickbreaker example
"""
import pygame as pg

class View:
    WIDTH = 800
    HEIGHT = 600

    """ A view of brick breaker rendered in a pg window """
    def __init__(self, model):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pg.Color(0,191,255))
        for item in self.model.items:
            self.screen.blit(item.image, item.rect)
        pg.display.update()
