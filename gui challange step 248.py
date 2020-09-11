
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class gui(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(850,325))

        self.master.title('Check files')
        self.master.config(bg='lightgrey')

        self.master.protocol("WM_DELETE_WINDOW",lambda: ask_quit(self))
        arg = self.master

if __name__ == "__main__":
    root = tk.Tk()
    App = gui(root)
    root.mainloop()
