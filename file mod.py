import time
import os
from pathlib import Path
import datetime

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(1)
file_change = mill - dt



print(file_change.strftime("%A, %B %d, %Y"))

curr = datetime.datetime.now()
print(curr)

p = Path("app.py")
p.stat()
p.stat().st_mtime
datetime.datetime.fromtimestamp(p.stat().st_mtime) 
t = datetime.datetime.fromtimestamp(p.stat().st_mtime)
print(t.strftime("%m/%d/%y at %I:%M"))
N = datetime.datetime.fromtimestamp(p.stat().st_mtime).isoformat()
print(N)

p2 = os.stat(p).st_mtime #this is the one we want
print(datetime.datetime.fromtimestamp(p2))


a = "C:/Users/Sarah/Desktop/foldera"
foldera = os.listdir(a)
b = "C:/Users/Sarah/Desktop/folderb"
folderb = os.listdir(b)
print(folderb)

now = datetime.datetime.now()
yesterday = datetime.timedelta(1)
then = now - yesterday
print(then)


dictionary = {}

def get_creationtime():
    return datetime.datetime.fromtimestamp(folderb.stat().st_mtime).isoformat()

for i in folderb:
    get_creationtime(i)
#for file in folderb:
#   file_time = get_creationtime(file)
#    file_date = file_time
#    dictionary[file] = file_date





#for filenames in os.walk("C:/Users/Sarah/Desktop/folderb"):
#    print('Files: ', filenames)

#req_format = datetime.strftime(curr,"%I : %M : %S")
#print(req_format)
#new = datetime.strftime(t,"%I : %M : %S")
#print(new)

 
