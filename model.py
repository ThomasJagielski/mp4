from frame import Frame

class Model:
    def __init__(self, mario):
        self.frame = Frame(0, 800)
        self.items = list()
        self.mario = mario

    def update(self):
        self.frame.update()
        self.mario.update()
