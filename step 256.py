import shutil
import os
import pytz
import time
import datetime
from pathlib import Path
from datetime import timedelta

source = r'C:/Users/Sarah/Desktop/foldera/'

destination = r'C:/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)



for i in files:
    absolute = os.path.join(source, i)
    modtime = os.path.getmtime(absolute)
    hours_24 = datetime.datetime.now() - timedelta(hours = 24)
    time_file = datetime.datetime.fromtimestamp(modtime)
    if hours_24 < time_file:
        shutil.copy(source+i, destination)
        print(time_file,i)


