

#this is my note
#I can comment on my code so everyone knows what I am doing
"""I use this for multy line code
this is note will continue
until I use the """



 ##alt + 3 comments out the code  on a line alt + 4 uncomments

"""docstrings are for users, like help menus"""

def printMe():
    """this is my docstring
"""
    
    print("meeeeeee!!")

print(printMe.__doc__)

#the docstring is called on by using __doc__ after the period

"""can use
help(printMe)

to pull up the information on the printMe function, along with any comments included in the code"""
