import sqlite3
import os


fileList = ['data.pdf', 'Hello.txt', 'information.docx', 'myImage.png', 'myMovie.mpg', 'myPhoto.jpg', 'World.txt']

path = "C:\\python_projects\\filelist"
dirs = os.listdir( path )


conn = sqlite3.connect('test9.db')
cur = conn.cursor()

conn = sqlite3.connect('test9.db')
with conn:
        conn = sqlite3.connect('test9.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtfile( ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename)')
        conn.commit()
conn.close()

conn = sqlite3.connect('test9.db')
with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_txtfile(col_filename) VALUES(?)", [file])
            print(file)   
            conn.commit()
conn.close()







    
    

