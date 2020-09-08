from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
#this function is telling us to pass in an arguement but we won't tell you how or what kind of
        #data it will be
        @abstractmethod
        def payment(self, amount):
            pass

class DebitCardPayment(car):
    #here we've defined how to implement the payment function from its parent paySlip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")

"""abstraction:
-data abstraction hides the complex details of items while only revealing the essential or relavant data.
-hides complex functionality through the use of creating abstract methods
-"they are defined but most of the time do not really contain any implementation"
-when a class contains more than one abstract method/function it is called an abstract class
-implementation of the abstract class is defined by a subclass or a third party plug in
-to use abstact base class you would import ABC, abstractmethod
-abstaction method useful for working on larg projects when child classes need to utilize implementation differently than it's parent class/other child classes
"""
