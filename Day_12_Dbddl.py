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

try:
    cursor = conn.cursor()
    cursor.execute("""create table department(
        dept_id int primary key,
        dept_name varchar(50),
        emp_name varchar(50));""")
    print("Table was created successfully !")

except Exception as e:
        print("Error:", e)

cursor.close()  
conn.close()
##################################

server = r'LAPTOP-151GUN5S'
database = 'hello'  

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;',
    autocommit=True
)

try:
    cursor = conn.cursor()
    cursor.execute("""insert into department(dept_id, dept_name, emp_name ) values
                   (1,'HR','Alice'),
                   (2,'IT','Oggy'),
                   (3,'Accounts','Charlie')""")
    print("The values were inserted into table department")

except Exception as e:
        print("Error:", e)

cursor.close()  
conn.close()



