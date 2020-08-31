import datetime

class Tryagain:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

    def age(self):
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/ 365
        return int(age_in_years)

if __name__ == "__main__":   
    tryagain = Tryagain("Dave Bowmen", "19710315")    
    print(tryagain.name)
    print(tryagain.age())


        
