from tkinter import *
import tkinter as tk
import webbrowser
import MakeYrOwn_fnct
import MakeYrOwn_gui
#here we have imported all the modules/widget we need to make this script work
#we have imported tkinter and it's classes, webbrowser so that the webbrowser will open on the
#users screen. we have also connected to the other files containing scripts

class MakeYrOwn(Frame):
    #here we create the funtion and pull in the parent class from tkinter
    def __init__(self,master,*args,**kwargs):
        #when it sees init it does the operation immediately below,
        #we pass in self as our class and master the parent class of frame
        Frame.__init__(self,master,*args,**kwargs) #arguments & keyword arguments are passed in

        self.master = master
        self.master.geometry('{}x{}'.format(700, 400)) #here we set the window size

        self.master.title('Make Your Own Website') #this is the title
        self.master.config(bg='lightgrey') #background color

        self.master.protocol("WM_DELETE_WINDOW",lambda: MakeYrOwn_fnct.ask_quit(self))
        #calls on a function in the fnct file that closes the window
        arg = self.master

        MakeYrOwn_gui.load_gui(self) #this loads the gui






if __name__ == "__main__":
    #we use this line to control our code flow, python will come here first and execute
    #whtat is underneath
    root = tk.Tk() #we have instantiated tiknter and have neamed it root
    App = MakeYrOwn(root) #here we pass it to app
    root.mainloop() #keeps the window open
