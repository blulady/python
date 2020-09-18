import shutil
import os
import pytz
import time
import datetime
from pathlib import Path
from datetime import timedelta

source = r'C:/Users/Sarah/Desktop/foldera/'
#this needs r before it for shutil to work
destination = r'C:/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)



for i in files:
    absolute = os.path.join(source, i)
    #here we join the path to the file name
    modtime = os.path.getmtime(absolute)
    #here we get the time that the file was last modified
    hours_24 = datetime.datetime.now() - timedelta(hours = 24)
    #gets the time representation of 24 hours ago
    time_file = datetime.datetime.fromtimestamp(modtime)
    #here we get the time representation of when the file was last modified
    if hours_24 < time_file:
        #if representation of 24 hours is less than the representation of the file's time of modification
        shutil.copy(source+i, destination)
        #copies the files from the sourc
        print(time_file,i)


