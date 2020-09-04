

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import studenttracking_fnct
import studenttracking_gui



class Student(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(700,400))

        self.master.title('Student Tracking')
        self.master.config(bg='lightyellow')

        self.master.protocol("WM_DELETE_WINDOW",lambda: studenttracking_fnct.ask_quit(self))
        arg = self.master

        studenttracking_gui.load_gui(self)


        
        
                             





if __name__ == "__main__":
    root = tk.Tk()
    App = Student(root)
    root.mainloop()
