#we have imported tkinter and it's classes, webbrowser so that the webbrowser will open on the
#users screen. we have also connected to the other files containing scripts

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import backup1_main
import backup1_fnct



def load_gui(self): #in this function that the main file calls, we use the tkinter methods  (label, grid and entry) to place/paint objects on the window
    self.btn_browse1 = tk.Button(self.master,width=12,text="Browse",command=lambda:backup1_fnct.directory(self))
    self.btn_browse1.grid(row=1,column=0,columnspan=2,padx=(10,10),pady=(10,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,text="Browse",command=lambda:backup1_fnct.directory(self))
    self.btn_browse2.grid(row=3,column=0,padx=(10,10),pady=(10,0),sticky=W)
    
    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda:backup1_fnct.ask_quit(self))
    self.btn_submit.grid(row=5,column=3,padx=(0,0),pady=(45,0),sticky=E)
    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Check Files',command=lambda:backup1_fnct.submit(self))
    self.btn_submit.grid(row=5,column=0,padx=(0,0),pady=(45,0),sticky=E)

    self.txt_subform = tk.Entry(self.master,text='',width=20,font=('Veranda',15))
    self.txt_subform.grid(row=1,column=1,columnspan=3,padx=(10,10),pady=(20,10),sticky=W+E+S)
    self.txt_wbdrct = tk.Entry(self.master,text='',width=20,font=('Veranda',15))
    self.txt_wbdrct.grid(row=3,column=1,columnspan=3,padx=(10,10),pady=(20,10),sticky=W+E+S)


if __name__ == "__main__":
    pass
    #we use this line to control our code flow, python will come here first and execute
    #whtat is underneath, in this case it is a pass because the main file is the only one we want executing
