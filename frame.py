from math import fabs

class Frame:
    def __init__(self, xmin, xmax):
        self.vx = 0.0
        self.range = [xmin, xmax]
        self.frame_of_view = self.range[1] - self.range[0]

    def update(self):
        self.range[0] += self.vx
        self.range[1] += self.vx
        if self.range[0] < 0.0:
            self.range[0] = 0.0
            self.range[1] = self.frame_of_view
