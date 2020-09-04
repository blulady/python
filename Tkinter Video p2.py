
import tkinter
from tkinter import *
#this second line imports all of tkinters widgets, if you knew specifically you could just call it
#http://effbot.org/tkinterbook/variable.html




class ParentWindow(Frame):
    def __init__ (self, master): 
        Frame.__init__ (self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')  #(bg='#00'), this line changes the background color



#how to create, use and call variables,
        #we'e going to create & effect the text in the textboxes by storing information to a string
        #and putting it in a text box
        self.varFName = StringVar()
        #we have instantiated and passed it to varFName
        self.varLName = StringVar()
        self.varFName.set("Bob")
        self.varLName.set("Smith")
        #here we set the variables aka assign a value
        print(self.varFName.get())
        print(self.varLName.get())
        #this is just for us, it comes up in the consol, the user won't see it
        #to get the varialb we havt to  write .get
        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        #here we are building our text box first we give it a name then we instantiate it, then we tell it where to go
        #() calls the class, it has several things  we can use to configure it
        #entry is a widget from Tkinter here we are calling the widget/class Entry() from Tkinter that we unpacked when we imported
        #self master is the entire window we have created
        #text will change by making it equal to the variable
        self.txtFName.pack()
        #the line above refrences the name to use it, then we used different types of geometry painters
        #to paintsomething on a form or window, pack places it but grid is more specific on placement
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.pack()
        #if you want to get the value from the text box you would use get like you did in line 31 self.varFName.get()
        #and that's how you would store it into it's variable 
        

        
        
if  __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
