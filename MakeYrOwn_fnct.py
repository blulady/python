#here we have imported all the modules/widget we need to make this script work
#we have imported tkinter and it's classes, webbrowser so that the webbrowser will open on the
#users screen. we have also connected to the other files containing scripts
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
                    </html>'.format(var_submission)
   var_direct = self.txt_wbdrct.get()
   f = open("MakeYrOwn.html","w")
   f.write(page_txt)
   f.close
   url = '{}/MakeYrOwn.html'.format(var_direct)
   webbrowser.open_new_tab(url)
   
   
#   with open(file_path, 'w' as f:
#             f.write(page_txt)
#(begin the process to create the file in a designated folder)

if __name__ == "__main__":
    pass
    




   
