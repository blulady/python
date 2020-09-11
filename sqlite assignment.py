#to communicate w/SQLite you have to import the module & connect to the db
import sqlite3
connection = sqlite3.connect("test_database.db")
#if the db you are connected to doesn't exist it will be created when the connect() function is executed
#here we have created a new db named test_database.db
#but you connect to an existing db in the same way
c = connection.cursor()
#this would be a way to communicate across the connection
#this line instantiates a cursor object
#a cursor is a control structure that enables operations on a db
#the coursor object "c" will let us execute commands on our SQL db "test_database" & return results

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

#here we execute regular SQL statements on the db through the cursor
#this line creates a new table named people and inserts three new columns into the table
#keep IDLE open with this code you wrote for the next step

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

#here we insert data into the table, a new row

connection.commit()
#here we commit the change so that it saves & now we could shut IDLE down & restart it

connection = sqlite3.connect(':memory:')
#this is how you create a database in temporary RAM

c.execute("DROP TABLE IF EXISTS People")
#this is how we delete the people table, we have first checked to see if it exists to preven errors that
#would occure if we tried to delete a table that doesn't exist

connection.close()
#this is how we close the connection: pushing out any changes/freeing up memory resources

with sqlite3.connect("test_database.db") as connection:
    #use with to open sqlite like other files
    #perform any SQL operations using this connection here
    #no longer need to commit()changes, they are automatically saved
    #you will still need to commit() a change if you want to see the result of that change immediately
    #before closing

#if you want to run more than one line of SQL code at a time 1. use executescript() method &
# give it a string that represents a full script, you separate the lines of code with semicolons to
#pass a multiline string for readability
import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                                CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT);
                                INSERT INTO People VALUES('Ron', 'Obvious', '42');
                                """

#we can also execute many similar statements by using the executemany() method & supplying a tuple
#of tuples where each inner tuple supllies info for a single command ie
peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
                    
c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
#we can then insert of all of these people at once
#after preparing our connection & our People table bys using this single line
#here the question mark acts as a place holder for the tuples in peopleValues
#this is called a parameterized statement
#the difference between parameterized & non-parameterized code is similar to how we write out strings
#by concatenate many parts together vs using the string format() method to insert specific pieces
#into a string after creating it


              
          
