#Python Ver: 3.8.3
#
#Author:    Daniel A. Christie
#
#Purpose:   Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#                   using Tkinter Parent and Child relationships
#
#Tested OS: This code was written & tested to work with Windows 10.

from tkinter import *
import tkinter as tk


#Be sure to import our other modules
#so we can have access to them

import phonebook_gui
import phonebook_func


#Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuratation
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500, 300)
        #This CenterWindeow method will center our app on the upper's screen
        phonebook_func.center_window(self,500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.confiugre(bg="#F0F0F0")
        #This protocol method is a tikinter built-in method to catch if
        #the user clicks the upper conter, "X" on Windos OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module.
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
