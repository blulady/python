

from abc import ABC, abstractmethod

class Fruit(ABC):
    def FruitQuantities(self, amount):
        print("There are: ",amount)

        @abstractmethod
        def quantity(self, amount):
            pass

class apples(Fruit):
    def numbers(self, amount):
        print("You have {} apples".format(amount))

obj = apples()
obj.numbers("80 boxes")
obj.numbers("80 boxes")

