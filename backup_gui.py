from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import backup_main
#import backup_fnct


def load_gui(self):
    self.lbl_name = tk.Label(self.master,text="Back Folder")
    self.lbl_name.grid(row=0,column=1,padx=(10,0),pady=(10,0),sticky=N)
    self.lbl_drctry = tk.Label(self.master,text="Select Folder for Backup")
    self.lbl_drctry.grid(row=2,column=2,columnspan=2,padx=(10,10),pady=(10,10),sticky=N+W)
    self.lbl_drctry2 = tk.Label(self.master,text="Backup Destination Folder")
    self.lbl_drctry2.grid(row=5,column=2,columnspan=2,padx=(10,10),pady=(10,10),stick=S+W)


    
    #self.btn_select = tk.Button(self.master,width=12,height=2,text='Select',command=lambda:backup_fnct.select(self))
    #self.btn_select.grid(row=2,column=2,padx(10,10),pady=(20,20),sticky=E)
    #self.btn_select2 = tk.Button(self.master,width=12,height=2,text='Select',command=lambda:backup_fnct.select(self))#will this need to be fnct.select2
    #self.btn_select2.grid(row=5,column=2,padx(10,10),pady=(20,20),sticky=E)


if __name__ == "__main__":
    pass

    

    
