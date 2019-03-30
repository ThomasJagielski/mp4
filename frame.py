from math import fabs

class Frame:
    def __init__(self, xmin, xmax):
        # initialize the change in x to 0
        self.vx = 0.0
        # set the view of the frame with the x and y position
        self.range = [xmin, xmax]
        # get the width of the frame
        self.frame_of_view = self.range[1] - self.range[0]

    def update(self):
        # add the change in x to both the xmin and xmax
        self.range[0] += self.vx
        self.range[1] += self.vx
        # unable to move to the left past the initial starting position
        if self.range[0] < 0.0:
            self.range[0] = 0.0
            self.range[1] = self.frame_of_view
