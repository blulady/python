
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
        self.lblFName = Label(self.master, text = 'First Name: ', font =("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblFName.grid(row =0, column=0, padx=(30,0), pady=(30,0))
        #to get the name to move in from the left edge we use padx & pady
        #we put padx following the grid locations, here we have moved it 10 pixels, x is horizantal, y is up/down
        
        #http://effbot.org/tkinterbook/grid.htm
        
        self.lblLName = Label(self.master, text = 'Last Name: ', font =("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblLName.grid(row =1, column=0, padx=(30,0), pady=(30,0))

        
        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column =1, padx=(30,0), pady=(30,0))
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row =1, column =1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2)
                                #invoking the button class
        self.btnSubmit.grid(row =2, column =1, padx=(0,0), pady=(30,0), sticky = NE)
        #use graphic software for a more complex information like paint to make a model of what I want then
        #use grid lines  to line columns up using row span ie colspan = 2 (you are using two colomns)
        #sticky - as to where on the window we want the bttn to stick to north is up east is right left is west south is down
        #change the button size after "submit" with the width statment and a height statement

         

        
        
if  __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
