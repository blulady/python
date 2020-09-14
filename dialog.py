from tkinter import *
import tkinter as tk
import dialog


class Maybe(Frame):
    def __init__ (self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(700,400))

        self.master.title('Try This?')
        self.master.simpledialog.askfloat()

        

if __name__ == "__main__":
    root = tk.Tk()
    App =Maybe(root)
    root.mainloop()
