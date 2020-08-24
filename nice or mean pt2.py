#
# Python 3.8.3
#
#
#formatting wild cards
#
#




def start():
    print("Hello {}".format(get_name()))
#by using {} and the format in the same line, the computer will substitute  the variable into the wildcard {}
    


def get_name():
    name = input("What is your name?   ")
    return name









if __name__ == "__main__":
    start()
    
