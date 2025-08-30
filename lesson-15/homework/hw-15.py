# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
import pyodbc
connection = pyodbc.connect("Driver={SQL Server};"
                      "Server=CMWST07;"
                      "Trusted_Connection=yes;")

cursor = connection.cursor()

sql = 'create database newpy_db'  
q1 = 'use newpy_db' 
q2 = 'create table Roster(name text, species text, age int)'

cursor.execute(sql)
cursor.execute(q1)
cursor.execute(q2)
cursor.close()
connection.commit()
connection.close()

## using sqlite

import sqlite3

with sqlite3.connect('newpy_db.sqlite') as connection:
    cursor = connection.cursor()

    query = ['create table Roster(name text, species text, age int)']
    for i in query:
        cursor.execute(i)

# 2. Populate your new table with the following values

import sqlite3

with sqlite3.connect('newpy_db.sqlite') as connection:
    cursor = connection.cursor()

    query = ["insert into Roster values('Benjamin Sisko','Human', 40)", "insert into Roster values('Jadzia Dax','Trill', 300)","insert into Roster values('Kira Nerys','Bajoran', 29)"]
    for i in query:
        cursor.execute(i)


# 3. Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

with sqlite3.connect('newpy_db.sqlite') as connection:
    cursor = connection.cursor()

    query = ["update Roster set name = 'Ezri Dax' where age = 300"]
    for i in query:
        cursor.execute(i)

# 4. Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

with sqlite3.connect('newpy_db.sqlite') as connection:
    cursor = connection.cursor()

    query = "select name, age from Roster where species = 'Bajoran'"
    result = cursor.execute(query)
    
    row = result.fetchall()
    print(row)

