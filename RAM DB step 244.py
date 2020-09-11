import sqlite3
connection = sqlite3.connect(":memory:")
c = connection.cursor()
c.execute("CREATE TABLE Roster_tbl(Name TEXT, Species TEXT, IQ INT)")
peopleValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas','Meat Popsicle',100),("Ak'not", 'Mangalor', -5))
c.executemany("INSERT INTO Roster_tbl VALUES(?, ?, ?)", peopleValues)
c.execute("UPDATE Roster_tbl SET Species=? WHERE Name=? AND IQ=?",
          ('Human', 'Korben Dallas', 100))
c.execute("SELECT Name, IQ FROM Roster_tbl WHERE Species = 'Human'")
for row in c.fetchall():
    print(row)
    
