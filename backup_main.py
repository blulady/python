from tkinter import *
import tkinter as tk
import backup_gui



class Backup(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(600,400))

        self.master.title('Backup')

        self.master.protocol("WM_DELETE_WINDOW",lambda: backup_fnct.ask_quit(self))

        arg = self.master

        backup_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = Backup(root)
    root.mainloop()



        

        
