"""kwargs is short for 'keyword arguments', a special syntax just like *args, written as
    **kwargs where the asterisks** represent a key value pair
    can be used to pass any number of undefined arguments into a function
    acts as a dictionary: maps out the value to the corresponding variable key
    https://www.youtube.com/watch?v=kB829ciAXo4"""

def myFun(**kwargs):
    print("kwargs", kwargs)
    myFun(first = "1", second = "2", third = "3")


def person(name, **data):
    print(name)
    print(data)

person('navin', age=28, city='mumbai', mob=9865432)

