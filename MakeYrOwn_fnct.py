import webbrowser
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import MakeYrOwn_main
import MakeYrOwn_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Are We Done Now?"):
        self.master.destroy()
        os._exit(0)


def submit(self):
   var_submission =  self.txt_subform.get().title()
   page_txt = '<html>\
                                <body>\
                                        <h1>\
                                                {}\
                                        </h1>\
                                </body>\
                    </html>' .format(var_submission)
   
    f = open("MakeYrOwn.html","w")
    f.write(page_txt)
    f.close

url = 'file:///Python/Python38-32/MakeYrOwn.html'
webbrowser.open_new_tab(url)

"""f.write("\
    <html>\
                <body>\
                        <h1>\
                            {}\
                        </h1>\
                </body>\
    </html>".format(var_submission)
    f.close()
           f = open("MakeYrOwn.html","r")
           url = 'file:///C:/Users/Sarah/AppData/Local/Programs/Python/Python38-32/MakeYrOwn.html'
           webbrowser.open_new_tab(url)"""


if __name__ == "__main__":
    pass
    




   
