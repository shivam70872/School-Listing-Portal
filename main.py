import tkinter as tk
from tkinter import messagebox
from student import add_student, view_all_students, search_student, update_student, delete_student

# Function for adding student
def add_student_gui():
    name = name_entry.get()
    roll_number = roll_number_entry.get()
    branch = branch_entry.get()
    year = year_entry.get()
    contact_number = contact_number_entry.get()
    
    try:
        add_student(name, roll_number, branch, year, contact_number)
        messagebox.showinfo("Success", "Student added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Function for viewing all students
def view_students_gui():
    # Clear the current contents of the listbox
    listbox.delete(0, tk.END)
    
    # Fetch the student data from the database
    data = view_all_students()
    
    # Insert the fetched data into the listbox
    for student in data:
        listbox.insert(tk.END, f"{student[1]} ({student[2]}) - {student[3]} - Year {student[4]} - {student[5]}")

# Function for searching students
def search_student_gui():
    keyword = search_entry.get()
    results = search_student(keyword)
    listbox.delete(0, tk.END)
    for student in results:
        listbox.insert(tk.END, f"{student[1]} ({student[2]}) - {student[3]} - Year {student[4]} - {student[5]}")

# Function for updating student
def update_student_gui():
    try:
        # Get the student ID and ensure it's a valid integer
        id = int(id_entry.get())  # This ensures that the ID entered is a valid integer
        
        # Now, get other details
        name = name_entry.get()
        roll_number = roll_number_entry.get()
        branch = branch_entry.get()
        year = int(year_entry.get())  # Ensure year is an integer
        contact_number = contact_number_entry.get()
        
        # Call the update function
        update_student(id, name, roll_number, branch, year, contact_number)
        messagebox.showinfo("Success", "Student updated successfully!")
        
    except ValueError:
        # This will catch cases where ID or year are not valid integers
        messagebox.showerror("Error", "Please enter valid integers for ID and Year.")
    except Exception as e:
        # This will catch other general exceptions
        messagebox.showerror("Error", f"Error: {e}")

# Function for deleting student
def delete_student_gui():
    try:
        id = int(id_entry.get())  # Ensure ID is an integer
        delete_student(id)
        messagebox.showinfo("Success", "Student deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Setting up the main window
root = tk.Tk()
root.title("Student Management System")

# Frames for organizing widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# Labels and Entries for Student Details
name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

roll_number_label = tk.Label(frame, text="Roll Number:")
roll_number_label.grid(row=1, column=0, padx=5, pady=5)
roll_number_entry = tk.Entry(frame)
roll_number_entry.grid(row=1, column=1, padx=5, pady=5)

branch_label = tk.Label(frame, text="Branch:")
branch_label.grid(row=2, column=0, padx=5, pady=5)
branch_entry = tk.Entry(frame)
branch_entry.grid(row=2, column=1, padx=5, pady=5)

year_label = tk.Label(frame, text="Year:")
year_label.grid(row=3, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1, padx=5, pady=5)

contact_number_label = tk.Label(frame, text="Contact Number:")
contact_number_label.grid(row=4, column=0, padx=5, pady=5)
contact_number_entry = tk.Entry(frame)
contact_number_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons for Add and Update actions
add_button = tk.Button(frame, text="Add Student", command=add_student_gui)
add_button.grid(row=5, column=0, padx=5, pady=10)

update_button = tk.Button(frame, text="Update Student", command=update_student_gui)
update_button.grid(row=5, column=1, padx=5, pady=10)

# Search section
search_label = tk.Label(frame, text="Search Student:")
search_label.grid(row=6, column=0, padx=5, pady=5)
search_entry = tk.Entry(frame)
search_entry.grid(row=6, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text="Search", command=search_student_gui)
search_button.grid(row=7, column=0, padx=5, pady=10)

# ID field for update/delete
id_label = tk.Label(frame, text="Student ID (for Update/Delete):")
id_label.grid(row=8, column=0, padx=5, pady=5)
id_entry = tk.Entry(frame)
id_entry.grid(row=8, column=1, padx=5, pady=5)

# Place the Delete button below the ID field
delete_button = tk.Button(frame, text="Delete Student", command=delete_student_gui)
delete_button.grid(row=9, column=0, columnspan=2, pady=10)  # This places the delete button below the ID field

# Listbox to display results
listbox = tk.Listbox(root, width=70, height=10)
listbox.pack(pady=10)

# View all students button
view_button = tk.Button(root, text="View All Students", command=view_students_gui)
view_button.pack()

# Start the Tkinter event loop
root.mainloop()
