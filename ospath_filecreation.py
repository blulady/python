import os

#were going to create a string and store it in a variable  https://docs.python.org/3.8/library/os.html

fName = 'hello.txt' #filename

fPath = 'C:\python_projects\\'  #file path, don't forget to escape the escapes (the \ by adding a \)

# we are going to use the two of these to create an absoulte file path not just a string
#https://docs.python.org/3/library/os.path.html
#  os.path.join(path, *paths)


#os.path.join(fPath, fName) #want it in the order it creats a file

abPath = os.path.join(fPath, fName)
print(abPath)
