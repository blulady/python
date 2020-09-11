#Parameterizing statements
#-good for hard to predict cases that can break SQL table
#-to avoid this we use placeholders in our SQLcode & insert the person data as a tuple
import sqlite3
        
#get personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
          (45, 'Luigi', 'Vercotti'))

#update the conent of a row using SQL UPDATE
#here we change the age of a person already in our People table (for a cursor w/in a connection)



    
