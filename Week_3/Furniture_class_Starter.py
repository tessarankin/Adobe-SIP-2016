# class Furniture
# attr: size, colour, comfiness, whether_or_not_there_is_handles
# methods: sit, slouch, watch_TV, lose_your_everything, be_pushed_off_by_your_dog

class Furniture():
    def __init__(self, size, colour, comfort, handles=False, furniture_name):
        self.size = size
        self.colour = colour
        self.comfort = comfort
        self.handles = False
        self.furniture name = furniture_name

    def be_pushed_off_by_your_dog(self,furnityre_name):
        print("Your dog pushed you off your " + self.furniture_name + ". This is war!")

    def sit(self):
        print("You sat on your " + self.furniture_name + ".")

Couch = Furniture()

