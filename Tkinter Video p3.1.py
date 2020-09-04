
import tkinter
from tkinter import *




class ParentWindow(Frame):
    def __init__ (self, master): 
        Frame.__init__ (self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')  




        self.varFName = StringVar()
        self.varLName = StringVar()


        #here we delete this to empty the text box
        #self.varFName.set("Bob")
        #self.varLName.set("Smith")
        #print(self.varFName.get())
        #print(self.varLName.get())

        self.lblFName = Label(self.master, text = 'First Name: ', font =("Helvetica", 16), fg='black', bg='lightblue')
        #we are not assigning this as a variable  so we don't have to self.varFName =StringVar()
        #but we do need to instantiate a label object
        #we need to assign the properties as to how to configure
        #then we have to paint it see the next line down
        self.lblFName.grid(row =0, column=0)
        #have to use grid can't mix with pack
        self.lblLName = Label(self.master, text = 'Last Name: ', font =("Helvetica", 16), fg='black', bg='lightblue')
        self.lblLName.grid(row =1, column=0)

        
        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid()
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid()


        #self.txtLName.pack() #here we used this because it didn't require extra parameters we're just
        #going to stack them up in the middle on top of each other
         

        
        
if  __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
