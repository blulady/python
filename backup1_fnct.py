
import webbrowser
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import backup1_main
import backup1_gui



def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Are We Done Now?"):
        self.master.destroy()
        os._exit(0)

def directory(self):
    self.directory = filedialog.askdirectory(initialdir="/",title="Select a Directory")
    #self.txt_subform = Entry(self, text=self.directory)


if __name__ == "__main__":
    pass
    




   
