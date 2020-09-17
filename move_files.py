import shutil
import os


source = r'C:/Users/Sarah/Desktop/foldera/'

#set the destination path to folder b
destination = r'C:/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)

for i in files:
    
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)


"""#set where the source of the files are
source = '/Users/Sarah/Desktop/foldera/'

#set the destination path to folder b
destination = '/Users/Sarah/Desktop/folderb/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)"""




