from db import connect

def add_student(name, roll_number, branch, year, contact_number):
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, roll_number, branch, year, contact_number) VALUES (%s, %s, %s, %s, %s)"
    values = (name, roll_number, branch, int(year), contact_number)
    try:
        cursor.execute(sql, values)
        conn.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
        



def view_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

def search_student(keyword):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM students WHERE name LIKE %s OR roll_number = %s"
    values = (f"%{keyword}%", keyword)
    cursor.execute(query, values)
    data = cursor.fetchall()
    conn.close()
    return data


def update_student(id, name, roll_number, branch, year, contact_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""UPDATE students SET name=%s, roll_number=%s, branch=%s, year=%s, contact_number=%s
                      WHERE id=%s""", (name, roll_number, branch, year, contact_number, id))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()
