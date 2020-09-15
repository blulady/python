import time
import os
from pathlib import Path
from datetime import datetime
p = Path("app.py")
p.stat()

p.stat().st_mtime

datetime.fromtimestamp(p.stat().st_mtime) 



print(datetime.fromtimestamp(p.stat().st_mtime))

t = datetime.fromtimestamp(p.stat().st_mtime)

print(t)

time.striftime("%I : %M : %S")

curr = datetime.now()

req_format = datetime.strftime(curr,"%I : %M : %S")

print(req_format)

new = datetime.strftime(t,"%I : %M : %S")

print(new)
