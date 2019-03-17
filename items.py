class Items:

    def __init__(self, model, image, x=0, y=0):
        self.model = model
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
