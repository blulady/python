

class  Game:  #after class python expects a name, naming conventions capitalize this
    variable1 = 'Hello'  #are considered constants because they are variables to this class
    variable2 = 'World' 

#here we have defined a class "Game" and stated teh blueprints to make a game object
#doesn't do anything by itself, you have to instantiate to build the object into being




if __name__ == "__main__":
    x = Game() #building an object and giving it the name of x
    #this is where you instantiate an object
    #can have multiple instantiations of an object
    print(x.variable1)
    print("{} {}".format(x.variable1, x.variable2))
