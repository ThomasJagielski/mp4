from items import Items

class Decorations(Items):
    def __init__(self, x = 0, y = 0):
        """ Initialize the position of the decoration with an x and y coordinate"""
        # intialize an x and y position of the decoration
        self.x = x
        self.y = y

    def update(self):
        pass
