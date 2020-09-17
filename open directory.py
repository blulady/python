from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('open directory')


def directory():
    root.directory = filedialog.askdirectory(initialdir="/",title="Select a Directory")
    label = Label(root, text=root.directory)
    label.pack()

b1 = Button(root, text="Browse", command = directory)
b1.pack()

root.mainloop()
