class Frame:
    def __init__(self, xmin, xmax):
        self.vx = 0
        self.range = [xmin, xmax]

    def update(self):
        self.range(0) += vx
        self.range(1) += vx
