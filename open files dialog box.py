from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('open file')



def files():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes=(("txt files", "*.txt"),("all files", "*.*"))) #C:\folder\address
    my_label = Label(root, text=root.filename)
    my_label.pack()


b1 = Button(root, text="File Open", command = files)
b1.pack()


root.mainloop()

