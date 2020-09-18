
import webbrowser
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os

import backup1_main
import backup1_gui



def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Are We Done Now?"):
        self.master.destroy()
        os._exit(0)



def directory(self):
    global source
    source = filedialog.askdirectory(initialdir="/",title="Select a Folder")
    self.txt_subform.insert(END, source)
    print(type(source))
    print(source)
    



def directory2(self):
    global dstn
    dstn = filedialog.askdirectory(initialdir="/",title="Select a Folder")
    self.txt_wbdrct.insert(END, dstn)
    print(dstn)

def submit(self):
    files = os.listdir(source)
    for i in files:
        absolute =os.path.join(source,i)
        shutil.copy(absolute, dstn)
    
    #source = self.txt_subform.insert #may need to add r
    #dstn = self.txt_subform.insert #may need to add r

    #files = os.listdir(source)
    #for i in files:
        #shutil.copy(source+i, dstn)
    


if __name__ == "__main__":
    pass
    




   
