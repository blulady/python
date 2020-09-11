import sqlite3
#how to retrieve info from python
peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

#select all first & last names from people over age 30
    #we use fetchall() on our cursor to retrieve the results of this query, which are stored as a list
    #of tuples
    #it loops over the rows in this list to view the individual tuples
    c.execute("SELECT FirstName, LastName FROM People WHERE Age>30")
    for row in c.fetchall():
        print (row)
