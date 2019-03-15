from frame import Frame

class Model:
    def __init__(self):
        self.frame = Frame(0, 800)
        self.items = list()

    def update(self):
        self.frame.update()
