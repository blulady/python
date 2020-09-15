import time
import os
from pathlib import Path
import datetime
from datetime import datetime



curr = datetime.now()
print(curr)

p = Path("app.py")
p.stat()
p.stat().st_mtime
datetime.fromtimestamp(p.stat().st_mtime) 
t = datetime.fromtimestamp(p.stat().st_mtime)
print(t)


mill = datetime.date(2000, 1, 1)
print(mill)
#req_format = datetime.strftime(curr,"%I : %M : %S")
#print(req_format)
#new = datetime.strftime(t,"%I : %M : %S")
#print(new)

 
