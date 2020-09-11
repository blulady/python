"""creating a class in python:
creating a class of "user"
-use keyword class & then name variable names for attributes
-also need to give default values: can change w/each object so long as we provide methods to do so (these methods only belong to this class)

-methods will need eleements of the class to operate
	use self keyword to pass them into a function
	self represens an instance of the class aka object"""
class User:
#define the attributes of the class
    name = 'no name provided'
    email = ' '
    password = '1234abcd'
    account = 0

#define the methods of the class
def login(self):
	entry_email = input("Enter your email: ")
	entry_password = input("enter your password: ")
	if(entry_email == self.email and entry_passoword == self.pasword):
		print("Welcome back, {}!".format(self.name))
	else:
		print("You are not authorized for this page.")
#outside of this class you would create an instance of the user class
new_user = User()

def __init__ (self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account

New_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
