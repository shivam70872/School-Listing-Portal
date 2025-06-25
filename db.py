import mysql.connector

def connect():
    return mysql.connector.connect(
        host="127.0.0.1",         # or your host
        user="root",     # replace with your MySQL username
        password="shivam123", # replace with your MySQL password
        database="project"  # replace with your database name
    )

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            roll_number VARCHAR(50) UNIQUE NOT NULL,
            branch VARCHAR(100),
            year INT,
            contact_number VARCHAR(20)
        )
    """)
    conn.commit()
    conn.close()
