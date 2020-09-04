import os
from tkinter import *
import tkinter as tk
import sqlite3


#be sure to import our other modules
#so we can have access to them

import phonebook_main
import phonebook_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    #get user's screen width and height
    #this is our own function to ceter the window
    screen_width = self.master.winfo_screenwidth()
    #screen_width = this is our name that we're giving it self.master = is tkinter's primary window, we have to write this to access its functions like winfo_screenwidth() - this gets the users window width & stores it in our own varable name
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    
    x = int((screen_width/2) - (w/2)) #this subtracts the arguements passed in from the other file (500,300) from the width of the  users screen that tkinter grabs with the winfo_screenwidth() function
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+()'.format(w, h, x, y))
    #centerGeo = the name we created  to call the geomentry method from the tkinter class, here substute the wild cards w/actual variables
    return centerGeo

#catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Ok to exit application?"): #exit program (the first text string) is going to be the windows name, the second screen will have the text in it
        #this is how we include a message in the exit window, again this is a function of the tkinter class we call when we say self
        #this closes app
        self.master.destroy() #the destroy() is called in from the tinkter class by self.master
        os._exit(0)#this takes all of our widgets and deletes it from the users memory to free up the memory 

#========================================================

def create_db(self): #this funtion builds the database and passes in self
    conn = sqlite3.connect('phonebook.db') #thise creates the db for the first time & connects it, here we create a class object call conn
    with conn: #with this connection do the following
        cur = conn.cursor()#this creates the cursor
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT, \
                col_lname TEXT, \
                col_fullname TEXT, \
                col_phone TEXT, \
                col_email TEXT \
                );"
        #you must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self) #have to call first run and pass in self to have access to the class objects

def first_run(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com') #dummy information to create the first row so the db isn't empty and we don't get any errors. this is a tuple called data
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor() #cursor is a function of  the sqlite3.connect
        cur,count = count_records(cur) #this is a function we create below, we have to pass in cur bc it is our connection to sqllite3 & access those functions we go down & grab it before continuing
        if count < 1: #if the count is less than 1, then we know our db to be empty then go ahead and put in the dummy info below
            our.execute("""Insert into tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe', '111-111-1111','jdoe@email.com')) #need to fix this
            conn.commit()
    conn.close()

def count_records(cur):
    count = "" #this makes our count empty
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""") #execute is a function from sqlite3 import the green text is the sql quierie 
    count = cur.fetchone() [0] #this accesses the database using the sqlite3 function fetchone() #this is the code to extract the count, we extract it because the data that gets returned as a tuple (to get the first section of a tuple, you have to call the first index
    return cur, count #return the cursor so you have access,  select count all from our database,

#select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget, whe the user goes to select something from the list, we created a listener bound it in the GUI &  called this function, needs self & event to gain access
    varList = event.widget #whatever is triggereing the event
    select = varList.curselection()[0] # here we are saying the varList selection (and again we put the tuple's initial indicie [0], the curseselection catches the index they click on but doesn't grab the actual text, so we
    #store the index as the variable select and pass that variable into the next variable/function
    value = varList.get(select) #this says to get the text of the value of select
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value]) #we select these columns from tbl where col_fullname = [value], value being what
        #was selected & select only the corrisponding user information that relates to the name that's selected
        varBody = cursor.fetchall()
        #this returns a tuple and we cna slice it into 4 parts using data[] during the iteration
        for data in varBody: #this is what part of the tuple we are accessing, these are the textboxes we are putting the information into
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)# this deletes the information in the box to clear it
            self.txt_lname.insert(0,data[1]) #this inserts the data
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self): #add to the list we currently have
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data to keep it consistent in the database
    var_fname = var_fname.strip()#this will remove any blank spaces befor and after the user's entry
    var_lname = var_lname.strip()#this will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) #combine our normalized names into a fullname and stores it in this variable
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: #will use this soon
       print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names len= if variable_fname  is greater than 0
        #and the length of the last name, phone and email are not empty then  
        conn = sqlite3.connect('db_phonebook.db') #if the previous statement passes then we connect to the db
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname)) # here we count it to see if it already exists
            count = cursor.fetchone()[0] #here we put the value (1 or 0) from the previous line into a variable
            chkName = count #here we put it in another variable
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName)) #user wont see this, remove it if you go live
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email)) #since the name isn't in the db, we put it in
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.") #else there will be an error message
        

def onDelete(self): #deletes things from the data base, is called on by a button in the gui
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value, stores the value of the curselection in a variable
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""") #count all rows from the tbl
        count = cur.fetchone()[0]
        if count > 1: 
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select)) #here is the sqlite3 command to delete the entry
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""") 
        count = cursor.fetchone()[0]
        i = 0
        while i < count: #while count is more than 0 do the following, this makes sure we only do the rows in our db otherwise we will get an error
                cursor.execute("""SELECT col_fullname FROM tbl_phonebook""") #count everything in the database # select the col_fullname bc that is what we have in the listbox
                varList = cursor.fetchall()[i]
                for item in varList: #varlist is the cursor item of the i
                    self.lstList1.insert(0,str(item)) #put the name in the list box
                    i = i + 1 #i continues to get bigger until it is bigger than our count (the count starts at the index 0)
    conn.close()


def onUpdate(self):
    try: 
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value -grab the index & actual text of what is being selected by the user w/in the list box and store that as var value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.") #if there is an error this is what we'll tell the user
        return #cancels the request
    # The user will only be alowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))#checking to see if there is information in this colomn
            count = cur.fetchone()[0]#where we get the return value back
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed #here we compare the information
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)#here we clear the text boxes
                        conn.commit()#here we commit it to the  db
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else: #if the information has already been changed then
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else:#if phone number or email text boxes are empty
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass

                       
