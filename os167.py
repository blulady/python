


import os, sys, time

path = "C:\python_projects"
path2 = "C:\python_projects\doc.txt"
file1 = 'new.txt'

whoo = os.path.join(path, file1)

dirs = os.listdir( path )

for file in dirs:
        print(file)


for file in dirs:
    if file == "\*.txt":
        print(file)

moar_time = os.path.getmtime(whoo)
fun_time = time.ctime(moar_time)

modification_time = os.path.getmtime(path2)
local_time = time.ctime(modification_time)
print(path2 + " modified " + local_time)

print(whoo + " modified " + fun_time)

