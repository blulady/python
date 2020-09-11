import pytz
import datetime
from datetime import datetime

pacific = pytz.timezone('America/Los_Angeles')
local_date = pacific.localize(datetime.now())
print(local_date)
print(local_date.hour)
Portland = (local_date.hour)
print(Portland)

eastern = pytz.timezone('America/New_York')
dt_eastern = datetime.now(eastern)
#print(dt_eastern)
print(dt_eastern.hour)
New_York = (dt_eastern.hour)


Londontz = pytz.timezone('Europe/London')
dt_London = datetime.now(Londontz)
print(dt_London)
print(dt_London.hour)
London = (dt_London.hour)
print(London)


#shop_list = ['Portland','New_York','London']

#def clopin():
#    for i in shop_list:
#        print("{} is open.".format(i))
        
#clopin()

if  9 <= London <=17:
    print("London Branch is open")
else:
    print("London Branch is closed")

if  9 <= Portland <=17:
    print("Portland HQ is open")
else:
    print("Portland HQ is closed")

if  9 <= New_York <=17:
    print("New York Branch is open")
else:
    print("New York Branch is closed")

#from 9 to 17:00


