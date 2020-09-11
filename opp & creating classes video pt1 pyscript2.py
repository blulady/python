
#parent class
class Organisim():
    name = "Unknown"
    species = "Unknown"
    legs = None #special data type that you have to define
    arms = 0
    origin = "Unknown"
    carbon_based = True #boolen value

    def information(self):  #giving the class a method, self will give you access to methods & information with key word
        msg = "\nName: {} \n species: {} \nLegs: {}\nArms: {}\nDNA:  {}\nOrigin: {}\nCarbon Based: ".format(self.name,self.species,self.legs,self.dna,self.origin,self.carbon_based)
        return msg
        

#child class instance
class Human(Organisim): #we build on the parent class by putting organism in the paranthesis & it will have access to this information & can override info from the parent class
    name = 'MacGuyver'
    species = 'Homospaien'
    legs = 2
    arms = 2
    dna = "Sequence A"
    origin = 'Earth'
    
    def ingenuity(self): #defining a function, passing in our self object
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

#another class
class Dog(Organisim):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bit(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg
        
#another child class instance
class Bacterium(Organisim):
    name = 'X'
    species = 'bacteria'
    legs = 0
    arms = 0
    dna = "Sequence c"
    origin = 'Mars'

    def replication(self):
        msg = '\nCells begin to divide and multiply into two seperate organisms!'
        return msg



if __name__ == "__main__":
    human = Human() #giving it the name = human instantiating it =Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
