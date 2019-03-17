"""
Code adapted from example showed in class with the brickbreaker example
"""
import pygame as pg

class View:

    """ A view of brick breaker rendered in a pg window """
    def __init__(self, model):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        self.screen = pg.display.set_mode((800, 600))

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pg.Color(0,191,255))
        for item in self.model.items:
            try:
                if item.erase_me:
                    self.model.items.remove(item)
                else:
                    self.screen.blit(item.image, [item.x - self.model.frame.range[0], item.y])
            except AttributeError:
                self.screen.blit(item.image, [item.x - self.model.frame.range[0], item.y])
        self.screen.blit(self.model.mario.image, [400, self.model.mario.y])
        pg.display.update()
        pg.display.flip()
