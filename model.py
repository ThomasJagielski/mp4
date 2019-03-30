from frame import Frame

class Model:
    def __init__(self, mario):
        """ Initialize the model with a reference to mario """
        # initialize the frame to start at the x value of 0 and the y value of 800
        self.frame = Frame(0, 800)
        # initialize an empty list for the model's items
        self.items = list()
        # intialize the model's mario for interactions
        self.mario = mario
        # set kill_mario to false (used for goomba interaction)
        self.kill_mario = False
        # initialize the system with a false value of win
        self.win = False

    def update(self):
        """ Update the model's state """
        # update the frame of the model
        self.frame.update()
        # update mario
        self.mario.update()
        # add all items to Model's items list
        for item in self.items:
            item.update()
