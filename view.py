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
        # set the model for interactions
        self.model = model
        # set game display
        self.screen = pg.display.set_mode((800, 600))

    def draw(self):
        """ Draw the current game state to the screen """
        # check if mario is killed by a goomba or if he has won
        if not (self.model.kill_mario or self.model.win):
            # fill the scren with a shade of blue (color of the sky)
            self.screen.fill(pg.Color(0,191,255))
            for item in self.model.items:
                try:
                    if item.erase_me:
                        # remove items if there status erase_me is true
                        self.model.items.remove(item)
                    else:
                        # otherwise change the screen based on the model's changes
                        self.screen.blit(item.image, [item.x - self.model.frame.range[0], item.y])
                except AttributeError:
                    self.screen.blit(item.image, [item.x - self.model.frame.range[0], item.y])
            # overlay screen with the model of mario
            self.screen.blit(self.model.mario.image, [400, self.model.mario.y])
            # update the view of the screen
            pg.display.update()
            # update the full surface of the screen
            pg.display.flip()
        else:
            # load the image of gameover
            gameover = pg.image.load('media/Gameover.png')
            # rescale the image to fill the entire screen
            gameover = pg.transform.scale(gameover, (800, 600))
            # overlay the scren with the "gameover screen"
            self.screen.blit(gameover,[0,0])
            # update the display
            pg.display.update()
            # update the full surface of the screen
            pg.display.flip()
