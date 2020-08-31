
#didn't work, don't copy
class Animal:
    def __init__ (self,classification, name, legs):
        self.classification = classification
        self.name = name
        self.legs = legs
    def printanimal(self):
        print(self.name)

t = Animal("Mammal", "Dog", "four legs")
t.printanimal()

class Dog(Animal):
    def __init__ (self,classification,name, breed, weight, color):
        super().__init__(self,name,leg)
        self.classification = classification
        self.name = name
        self.breed = breed
        self.weight = weight
        self.color = color
        self.leg = leg

    def printname(self):
        print(self.breed)

x = Dog("Dog","Salty", "mixed terrier", "18lbs", "white","four legs")
x.printname()


