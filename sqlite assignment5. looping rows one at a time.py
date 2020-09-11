#here we want to loop our result rows one at a time instead of fetching them all at once
#modify code to use this method of process the results of SQL querry
import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection. cursor()
c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
                break
    print(row)

#this checks each time wheather our fetchone() returns another row from the cursor, displaying the row
    #breaking out of the loop once we run out of results
    #None keyword is the way Python represnts the absence of any value for an object
    #when we want to compare a string to a missing value we used empty quotes to check that the string
    #object had no information inside ie stringName == ""
    #when we want to compare other objects to missing values to see if they hold any information we
    #compare them to None
