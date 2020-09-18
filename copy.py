import shutil
import os


source = 'C:/Users/Sarah/Desktop/foldera/'

#set the destination path to folder b
destination = 'C:/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)

for i in files:
    
    #we are saying move the files represented by 'i' to their new destination
    shutil.copy(source+i, destination)
