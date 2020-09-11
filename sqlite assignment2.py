import sqlite3
#For instance, suppose we
#want to insert a person into our People table based on user-supplied information.
#get personal data from user

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db' as connection:
                     c = connection.cursor()
                     line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
                     c.execute(line)

#we had to change age into an integer to make sure there is a valid entry but then had
 #to change it back into a string to  concatenate it with the rest of the line
                    
