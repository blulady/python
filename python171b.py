import sqlite3
import os


fileList = ['data.pdf', 'Hello.txt', 'information.docx', 'myImage.png', 'myMovie.mpg', 'myPhoto.jpg', 'World.txt']

path = "C:\\python_projects\\filelist"
dirs = os.listdir( path )


conn = sqlite3.connect('test9.db')
cur = conn.cursor()

conn = sqlite3.connect('test9.db')
with conn:
    def create_table(self):
        conn = sqlite3.connect('test9.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtfile( ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename)')
        conn.commit()

conn = sqlite3.connect('test9.db')
with conn:
    def ad(self):
        for file in fileList:
            if file.endswith(".txt"):
                cur.execute("INSERT INTO tbl_textfile(col_filename) VALUES(?)", (file))
                print(file)   
        conn.commit()
conn.close()







    
    

