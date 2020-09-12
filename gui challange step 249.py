
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from tkinter import filedialog

class gui(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(850,325))

        self.master = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("all files", "*.*"))
                                                                                                    

       # self.master.overrideredirect(1)
        #title_bar = tk.Frame(self.master,bg= "darkgrey", relief=tk.SUNKEN,bd=0)

        self.master.title('Check files')
        self.master.config(bg='lightgrey')

        self.master.protocol("WM_DELETE_WINDOW",lambda: ask_quit(self))
        arg = self.master

        self.btn_browse1 = tk.Button(self.master,text='Browse...',width=15,height=1,font=("Helvetica",15))
        self.btn_browse1.grid(row=1,column=0,padx=(12,0),pady=(70,0),sticky=S)

        self.btn_browse2 = tk.Button(self.master,text='Browse...',width=15,height=1,font=("Helvetica",15))
        self.btn_browse2.grid(row=3,column=0,padx=(12,0),pady=(10,0),sticky=S)

        self.btn_check = tk.Button(self.master,text='Check for Files...',width=15,height=2,font=("Helvetica",15))
        self.btn_check.grid(row=6,column=0,padx=(40,0),pady=(5,0),sticky=W)

        self.btn_close = tk.Button(self.master,text='Close Program',width=15,height=2,font=("Helvetica",15))
        self.btn_close.grid(row=6,column=5,padx=(60,10),pady=(0,0),sticky=E+S)

        self.text_entry1 = tk.Entry(self.master,text='', width=35,font=("Helvetica",20))
        self.text_entry1.grid(row=1,column=1,rowspan=1,columnspan=5,padx=(50,0),pady=(10,0),sticky=W+E+S)

        self.text_entry2 = tk.Entry(self.master,text='',width=30,font=("Helvetica",20))
        self.text_entry2.grid(row=3,column=1,rowspan=2,columnspan=5,padx=(20,0),pady=(10,0),sticky=W+E+N+S)        
        

        
                                     

if __name__ == "__main__":
    root = tk.Tk()
    App = gui(root)
    root.mainloop()
