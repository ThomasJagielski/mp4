class Items:

    def __init__(self, model, image, x=0, y=0):
        """ Initialize the item class with a reference to the model, an image,
        and a position (defined by x and y) """
        # initialize the model for interactions between items
        self.model = model
        # set the image
        self.image = image
        # define a rectangle around the image
        self.rect = self.image.get_rect()
        # initialize the x and y position of the item
        self.x = x
        self.y = y

    def update(self):
        pass
