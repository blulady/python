
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

        self.lblLName = Label(self.master, text = 'Last Name: ', font =("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblLName.grid(row =1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text = ' ', font =("Helvetica", 16), fg='black', bg='lightgrey')
        #here we add another label so we invoke the label widget (Label()) & add parameters (what goes in
        #the (), text will equal the info in the variables fn/ln
        self.lblDisplay.grid(row=3, column =1, padx=(30,0), pady=(30,0))
        #here we "paint the label", using the grid 
        
        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column =1, padx=(30,0), pady=(30,0))
        
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row =1, column =1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command =self.submit)
        self.btnSubmit.grid(row =2, column =1, padx=(0,0), pady=(30,0), sticky = NE)
        #here is where we add functionality to the button by adding command =self.submit & then
        #creating the self.submit function

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command =self.cancel)
        self.btnCancel.grid(row =2, column =1, padx=(0,90), pady=(30,0), sticky = NE)
         #this is going to be the cancel button
        #to move this button further left so we are going to change to padx=(0,90)
        #here is where we add functionality to the button by adding command =self.cancel & then
        #creating the self.cancel function

    def submit(self):
        #this needs to be indented as the previous function under the class, we need to pass the self key to
        #make it part of the ParentWindow class ie self is the class, submit is the method
        #we need to grab the values in the text boxes so we need to put them in a temporary variable see next line
        fn = self.varFName.get()
        #firstname variable, we are grabing the text from it so we use self.varFName, get is the method we use
        #to grab the information that is stored in it
        ln = self.varLName.get()
        #here we have grabed the values stored in these text boxes and stored it to the variables fn/ln
        self.lblDisplay.config(text='Hello {} {}'.format(fn,ln))
        #here we want the output to selflabelDisplay, to dynamically change something in the middle of the
        #program while it is running you use the config() method/function
        #the parameters that we are sending it come from the variable fn/ln, using format with the string aka we have formated our varialbes into this string
        
    def cancel(self):
        #if someone clicks on cancel we want it to close the window
        self.master.destroy
        #destroy is the command to close the window
        
        
        
        

        
        
if  __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
