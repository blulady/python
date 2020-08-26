import sqlite3
import os


path = "C:\\python_projects\\filelist"
dirs = os.listdir( path )

for file in dirs:
    if file.endswith(".txt"):
       print(file)

conn = sqlite3.connect('test3.db')
cur = conn.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtfile( ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename)')
    
def tablestuff():
 
    cur.execute("INSERT INTO tbl_textfile(col_filename) VALUE (?)",('info'))
    conn.commit()
    c.close()
    conn.close()



create_table()
tablestuff()


    
    

