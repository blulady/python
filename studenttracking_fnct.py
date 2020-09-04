


import os
from tkinter import *
import tkinter as tk
import sqlite3

import studenttracking_main
import studenttracking_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Are We Through Yet?"):
        self.master.destroy()
        os._exit(0)

#=======================================================

def create_db(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",('Jay','Doe','Jay Doe','111-111-1111','jdoe@email.com','Python'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_student""")
    count = cur.fetchone()[0]
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_student WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()

        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def submit(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip().title()#can I put title() here?
    var_email = self.txt_email.get().strip().title()#can I put title() here?
    var_course = self.txt_course.get().strip().title()#this is my code
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and( len(var_course) > 0):
        conn = sqlite3.connect('db_student.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_student (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is a data in all five fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with, {} \n will be permanently deleted from the database. \n\nGet Rid of the Garbage?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_student.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and I won't let it go. \n\nPlease add another record so I won't be alone, then you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('db_student.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_student WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_student WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(col_course) FROM tbl_student WHERE col_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 == 0:
                response =messagebox.askokcancel("Update Request","The following changes ({}), ({}), and ({}) will be implement for ({}). \n\n Shall we do this?".format(var_phone,var_email,var_course,var_value))
                print(response)
                if reponse:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_student SET col_phone = '{0}',col_email = '{1}',col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Never Mind","We're not doing this to ({}) anymore.".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}), ({}) and ({}) \nalready exist in the database for this name. \n\nYour update has been tossed out the window.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, emal or course information.")
    onClear(self)


if __name__ == "__main__":
    pass
            
            
                            
        
