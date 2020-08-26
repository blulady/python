import sqlite3
import os


path = "C:\\python_projects\\filelist"
dirs = os.listdir( path )


conn = sqlite3.connect('test7.db')
cur = conn.cursor()

def create_table():
    conn = sqlite3.connect('test7.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtfile( ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename)')
    conn.commit()

def ad():
    for file in dirs:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_textfile(col_fulename) VALUES(?)", ('file'))
            print(file)   
    conn.commit()
conn.close()




create_table()



    
    

