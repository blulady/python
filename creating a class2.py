import datetime

class Buser:
    """for now we are only storing name & birthday but we will store more information later, this is a doc string
        and it will show up when we print help(Buser) - using the help function for this class
        https://www.youtube.com/watch?v=apACNr7DC_s"""
    
    def __init__(self, full_name, birthday):  #self is a reference to the new object being created
        self.name = full_name
        self.birthday = birthday

        #extract first and last names
        name_pieces = full_name.split(" ") #will chop th name into pieces whenever we hit a space and put those pieces into an array
        self.first_name = name_pieces[0]
        last_name = name_pieces[-1] #without using self we will get an attribute error, we didn't attach last name to the object using self


buser = Buser("Dave Bowman", "19710315")
print(buser.name)
print(buser.birthday)

        
#adding another method to the user class that will return the age of the Buser in years this is broken
"""def age(self):
            
    today = datetime.date(2001, 5, 12)
    yyyy = int(self.birthday[0:4])
    mm = int(self.birthday[4:6])
    dd = int(self.birthday[6:8])
    dob = datetime.date(yyyy, mm, dd)
    age_in_days = (today - dob).days
    age_in_years = age_in_days / 365
    return int(age_in_years)"""

def age(self):
    today = datetime.date(2001, 5, 12)
    yyyy = int(self.birthday[0:4])
    mm = int(self.birthday[4:6])
    dd = int(self.birthday[6:8])
    dob = datetime.date(yyyy, mm, dd)
    age_in_days = (today - dob).days
    age_in_years = age_in_days / 365
    return int(age_in_years)


buser = Buser("Dave Bowman", "19710315")
print(buser.name)
print(buser.age_in_years())
