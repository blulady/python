
from tkinter import *
import tkinter as tk

#Be sure to import our other modules
#so we can have access to them
import phonebook_main
import phonebook_func

def load_gui (self):
    #self is the key to access the class objects, perimissions to access widgets
    #we are giving the class all of these wigets; buttons, scroll bar, labels, textboxes
    self.lbl_fname = tk.Label(self.master, text='First Name: ')
    #tk.Label this is tkinters class for a label, this is the syntax to access it/instantiate it, then you have to name that instance (self.lbl_fname ), we put it on that window using self.master <syntax for the primary form, then we give it a text
    self.lbl_fname.grid(row=0,column-0,padx=(27,0),pady=(10,0),sticky=N+W)
    #here we place/paint it onto the screen using grid()
    self.lbl_lname = tk.Label(self.master, text = 'Last Name: ')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Addres: ')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_user = tk.Label(self.master, text='User: ')
    self.lbl_user.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text=' ')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        #since the text takes up more than on column span, here we specify 2
    self.txt_lname = tk.Entry(self.master,text=' ')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master,text=' ')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_email = tk.Entry(self.master,text=' ')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.scrolibarl = Scrolibar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0, yscrollcommand=self.scrollbar1.set)
    #here we define the tkinter listbox, we give it the name self.lstList1
    self.lstList1.bind('<<ListboxSelect>>',lambda event: phonebook_func.onSelect(self,event))
    #here we bind our list box to an event aka a listener, for a user to click or select an object to then call the function which in this case is a lambda anonymous function, which means we don't have to name the function, we just
    #throw in what it is going to do, here it will go into our phonebook_func script and call the onSelect() function, we pass in self(to access the class) and event because it is waiting for an event
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0), pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: phonebook_func.onUpdate(self))
    self.btn_updat.grid(row=8,column1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width-12,height=2,text='Close',command=lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8,column+4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    phonebook_func.create_db(self)
    #here we call on the phonebook_func.create_db w/all of our functions,, pass in the key (self)
    phonebook_func.onRefresh(self)
    #here we call onRefresh() pass in the key (self) w/the permissions

    if __name__ == "__main__":
        pass
    
    
                        
