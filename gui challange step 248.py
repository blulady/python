
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

class gui(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(850,325))

        myFont = font.Font(size=60)

       # self.master.overrideredirect(1)
        #title_bar = tk.Frame(self.master,bg= "darkgrey", relief=tk.SUNKEN,bd=0)

        self.master.title('Check files')
        self.master.config(bg='lightgrey')

        self.master.protocol("WM_DELETE_WINDOW",lambda: ask_quit(self))
        arg = self.master

        self.btn_browse1 = tk.Button(self.master,text='Browse...',width=24,height=2)
        self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(60,0),sticky=S)

        self.btn_browse2 = tk.Button(self.master,text='Browse...',width=24,height=2)
        self.btn_browse2.grid(row=3,column=0,padx=(25,0),pady=(10,0),sticky=S)

        self.btn_check = tk.Button(self.master,text='Check for Files...',width=24,height=4)
        self.btn_check.grid(row=5,column=0,padx=(40,0),pady=(10,0),sticky=W)

        self.btn_close = tk.Button(self.master,text='Close Program',width=24,height=4)
        self.btn_close.grid(row=5,column=8,padx=(60,0),pady=(0,0),sticky=E+S)

        self.text_entry1 = tk.Entry(self.master,text='', width=50)
        self.text_entry1.grid(row=1,column=1,rowspan=1,columnspan=6,padx=(50,0),pady=(10,0),sticky=W+E+S)

        self.text_entry2 = tk.Entry(self.master,text='',width=50)
        self.text_entry2.grid(row=3,column=1,rowspan=2,columnspan=6,padx=(20,0),pady=(10,0),sticky=W+E+N+S)        
        

        
                                     

if __name__ == "__main__":
    root = tk.Tk()
    App = gui(root)
    root.mainloop()
