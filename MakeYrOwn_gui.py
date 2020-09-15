#we have imported tkinter and it's classes, webbrowser so that the webbrowser will open on the
#users screen. we have also connected to the other files containing scripts

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import MakeYrOwn_main
import MakeYrOwn_fnct



def load_gui(self): #in this function that the main file calls, we use the tkinter methods  (label, grid and entry) to place/paint objects on the window
    self.lbl_subform = tk.Label(self.master,text="Please enter what you want on your website: ", font=('Helvetica', 16), fg='black', bg='lightgrey')
    self.lbl_subform.grid(row=0,column=1,columnspan=2,padx=(27,0),pady=(40,0),sticky=N+W) 
    self.lbl_wbdrct = tk.Label(self.master,text="Please enter what file location you want to store your website at: ",font=('Helvetica', 16), fg='black', bg='lightgrey')
    self.lbl_wbdrct.grid(row=5,column=1,columnspan=2,padx=(27,0),pady=(10,0),sticky=W)

    self.txt_subform = tk.Entry(self.master,text='',width=15,font=('Veranda',20))
    self.txt_subform.grid(row=3,column=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+W+E+S)
    self.txt_wbdrct = tk.Entry(self.master,text='',width=15,font=('Veranda',20))
    self.txt_wbdrct.grid(row=7,column=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+W+E+S)

    #in th lines below we call the Tkinter button widget & paint it on the main window

    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda:MakeYrOwn_fnct.submit(self))
    self.btn_submit.grid(row=8,column=2,padx=(0,0),pady=(45,0),sticky=E)

    if __name__ == "__main__":
        pass
    #we use this line to control our code flow, python will come here first and execute
    #whtat is underneath, in this case it is a pass because the main file is the only one we want executing
