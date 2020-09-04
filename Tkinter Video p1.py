





class ParentWindow(Frame):
    #create a child class that inherets  from Frame the parent class  within Tkinter
    #will be inhereting from tkinter
    def __init__ (self, master): # can add (self, master, **args, **kwargs)
    #passing in self is passing in the key so it has access to all the widgets within the class
    #master references Frame
    #init (initalize) has builtin functions and python recognizes it
        Frame.__init_ (self)

        self.master = master
        #you have to say self to reference the class items
        self.master.resizable(width=False, height=False)
        #this makes it so that when the first window comes out the user doesn't have a resizing option
        self.master.geometry('{}x{}').format(700, 400)
        #with the false statement, we can also give it a specific size & geomentry with the geometry statement
        #what we are saying here is that the user can't resize it and it will be 700 pixels by 400 pixels
        self.master.title('Learning Tkinter!')
        #just defining the class, we haven't instanciated it nor have called on anything
        
        
if __name__ == "__main__"
#use this line to control program flow, since python will skip all the previous code and come straight here
    root = Tk()
    #indent here,  we weill be calling a class, in this case Tkinter, name them with a capital
    #by writing Tk() we have called on a class object but we need to pass it to somthing
    #by calling on Tk() we have instantiated the class and now that instance of it is named root
    App = ParentWindow(root)
    #here we have attached app & ParentWindow to root
    #ParentWindow is comming from Tkinter because Frame is tkinter's main class, named it root
    #attached it to the parent window
    root.mainloop()
    #without mainloop, the window will pop open and then shut down again, mainloop keeps it looping
