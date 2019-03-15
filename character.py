from items import Items

class Character(Items):
    def __init__(self, model, vx, vy):
        self.model = model
        self.vx = vx
        self.vy = vy
