from items import Items

class Character(Items):
    def __init__(self, model, image, x=0, y=0, vx=0, vy=0):
        self.model = model
        self.image = image
        # set x and y position of the character
        self.x = x
        self.y = y
        # initialize a change in x and y
        self.vx = vx
        self.vy = vy
