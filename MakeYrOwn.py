from tkinter import *
import tkinter as tk
from tkinter import messagebox
import makeyrown_fnct
import makeyrown_gui


def MakeYrOwn(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(700,400))

        self.master.title('Make Your Own Website')
        self.master.config(bg='lightgrey')

        self.master.protocol("WM_DELETE_WINDOW",lambda: makeyrown_fnct.ask_quit(self))
        arg = self.master

        makeyrown_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = MakeYrOwn(root)
    root.mainloop()
