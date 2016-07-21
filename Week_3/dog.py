class Dog():

    #Constructor function/attruibutes
    def __init__(self, furColour, weight, eyeColour, name):
        self.furColour = furColour
        self.weight = weight
        self.eyeColour = eyeColour
        self.name = name

    #function/method
    def bark(self):
        print("Woof")

    def wag(self):
        print("Wagging tail")

    def run(self):
        print("Your dog is running")

Toto = Dog("Brown", 25, "Blue", "Toto")
Toto.run()
