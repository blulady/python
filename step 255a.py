import shutil
import os
import pytz
import time
import datetime
from datetime import datetime
from pathlib import Path

source = '/Users/Sarah/Desktop/foldera/'

destination = '/Users/Sarah/Desktop/folderb/'
files = os.listdir(destination)

p = Path("app.py")
#p.stat()
#p.stat().st_mtime
p2 = datetime.fromtimestamp(p.stat().st_mtime) 
print(p2)
#for i in files:
 #   print(i)
#for i in files:
    
p3 = os.stat(p).st_mtime #this is the one we want
print(datetime.fromtimestamp(p3))

for i in files:
    os.stat(i).st_mtime
    print(datetime.fromtimestamp(i))
    
