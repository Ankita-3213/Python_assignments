import pyodbc

server = r'LAPTOP-151GUN5S'
database = 'hello'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;',
    autocommit=True
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Userr (
    u_id int identity PRIMARY KEY,
    name varchar(50),
    age int
)
""")

cursor.execute("INSERT INTO Userr (name, age) VALUES (?, ?)", ("Alice", 30))

d = [("Bob",20),("Charlie",30),("Dave",18)]
cursor.executemany("INSERT INTO Userr (name, age) VALUES (?, ?)", d)

cursor.execute("SELECT * FROM Userr")
print(cursor.fetchall())

cursor.close()
conn.close()


