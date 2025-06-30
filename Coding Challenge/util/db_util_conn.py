import pyodbc

def get_connection():
    try:
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LAPTOP-151GUN5S;"       
            "DATABASE=PetPals;"
            "Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print("Database connection failed:", e)
        return None

