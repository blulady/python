import os, sys, time

path = "C:\python_projects"
dirs = os.listdir( path )

moar_time = os.path.getmtime(path)
fun_time = time.ctime(moar_time)

for file in dirs:
        print(file)

for file in dirs:
    if file.endswith(".txt"):
        whoo = os.path.join(path, file)
        print(whoo+ " " + fun_time)


#modification_time = os.path.getmtime(path)
#local_time = time.ctime(modification_time)
