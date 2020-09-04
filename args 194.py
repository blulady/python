"""ARG (short for arguments) is a special syntax written out at *args and used to pass in an
undefined number of arguments to a function. * represents any number of arguments in tuple form.
Args allow you to add on to your current parameters even if you didn't have any defined
ie"""

def myFun(*args):
    for arg in args:
        print(arg)
myFun('This is an example of args', "string", "and then an integer", 5)
