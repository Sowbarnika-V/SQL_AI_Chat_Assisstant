import sqlite3

# Connect to sqlite
connection=sqlite3.connect("ajackus.db")

# Cursor to insert and create record or tabel and retrieving
cursor = connection.cursor()


table1_info="""
 CREATE TABLE Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )
"""
cursor.execute(table1_info)

cursor.execute('''Insert Into Employees values(1, "Alice", "Sales", 50000, "2021-01-15")''')
cursor.execute('''Insert Into Employees values(2, "Bob", "Engineering", 70000, "2020-06-10")''')
cursor.execute('''Insert Into Employees values(3, "Charlie", "Marketing", 60000, "2022-03-20")''')


table2_info="""
CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
"""
cursor.execute(table2_info)

cursor.execute('''Insert Into Departments values(1, "Sales", "Alice")''')
cursor.execute('''Insert Into Departments values(2, "Engineering", "Bob")''')
cursor.execute('''Insert Into Departments values(3, "Marketing", "Charlie")''')


print('The inserted records are :')

data = cursor.execute('''Select * From Departments''')

for row in data:
    print(row)


connection.commit()
connection.close()