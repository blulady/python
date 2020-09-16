import time
import os
from pathlib import Path
import datetime
from collections import namedtuple

p = Path("C:/Users/Sarah/Desktop/foldera")
a = "C:/Users/Sarah/Desktop/foldera"
foldera = os.listdir(a)
b = "C:/Users/Sarah/Desktop/folderb"
folderb = os.listdir(b)

files = []

def get_modtime():
    for item in p.glob('**/*'):
        if item.suffix.isin(['.txt']):
            modtime = (datetime.datetime.fromtimestamp(item.stat().st_mtime))
            print(modtime)


