from items import Items

class Character(Items):
    def __init__(self, model, image, x=0, y=0, vx=0, vy=0):
        self.model = model
        self.image = image
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
