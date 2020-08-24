


def start(nice=0, mean=0,name =""): #both nice/mean recieve 0 as a numeric value,
    #name recieves an empty string, in this way we are controlling the default values,
    #w/o producing an error 
    #get users name
    name = describe_game(name) #function to pass name to (which is empty now)
    nice,mean,name = nice_mean(nice,mean,name) #creates fcnt nice_mean add adds the 3 variables
    #and passes the variable to it, 
    
def describe_game(name):
    """check if this is anew game or not, if it is then get the user's name if not then thank the player
         for playing again and continue w/game"""
    #meaning if we don't alread have this user's name, they are a new player and we need to get it
    #
    if name != "":
        #this says if name doesn't equal empty then print "thank you for playing again that way
        #we aren't explaining it again
        print("\nThank you for playing again {}!".format(name))
    else:
        #this says if name is empty ask for input
        stop = True
        #here we create the veriable of stop and give it the value of true
        while stop:
            #while stop is true do the following loop
            if name == "":
                #if name is empty
                name = input("\nWhat is your name?   \n>>>  ").capitalize() #capitalize() is a built in format to capitalize the word & plug that into name, also get name
                if name != "":
                    #if name is not empty print the following
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. n\You can choose to be nice or mean")
                    print("but at the end of the game your fat \nwill be sealed by your actions.")
                    stop = False
                    #stop this loop, we  already have the name 
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name) #calling a new function, passing in the variables
        pick = input("\nA stranger approches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>:  ").lower() #built in method to make the string lower case
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1) #nice was set to 0, now nice equals 1
            stop = False
        if pick == "m": 
            print ("n\The stranger glares at you  \nmenacingly and storms off...")
            mean = (mean + 1) #instead of nice, mean now equals 1
            stop = False
    score(nice,mean,name) #pass the 3 varibles to the score()

def show_score(nice,mean,name): #we are passing the variables in from (score)
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values sotred w/in the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables
        win(nice, mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name) :
    #substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
       #callin in .format you associate the wildcard w/the variable
    # call again function & pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name) :
    #subtract the {} wildcards with our bariable values
    print("n\Ahhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our veriables
    again(nice,mean,name) #sending them into again to ask if they want to play again
    

def again(nice,mean,name) :
    stop = True
    while stop:
        choice = input("\nDo you want to play again (y/n) : \n>>> ").lower() #get info from the user,
        #lower case whatever they give us and store it in the variable choice
        if choice == "y": 
            stop = False #if they enter yes, stop the loop
            reset(nice,mean,name) #create a reset function to restart the game
        if choice == "n":
            print("n\Oh, so sad, sorry to see you go!")
            stop = False #will stop the loop
            quit() #pull up function quit, if it was actually executible it would shut the program automatically
        else:
            print("n\Enter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")

def reset(nice, mean,name) :
    nice = 0 #reseting the variables for the beginning of a new game
    mean = 0
            #notice, i don't resent the name variable as that same user is still playing
    start(nice,mean,name)
    




if __name__ == "__main__":
    start()
