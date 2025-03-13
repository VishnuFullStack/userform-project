import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Function to submit the form data to MySQL
def submit_data():
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='user_data_db'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Insert query with values from the form
            query = "INSERT INTO user_registration (name, mobile, address, job_role, qualification, comments) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (entry_name.get(), entry_mobile.get(), entry_address.get(), entry_job_role.get(), entry_qualification.get(), entry_comments.get())
            cursor.execute(query, values)
            connection.commit()
            
            messagebox.showinfo("Success", "Data Submitted Successfully!")
    
    except Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to reset the form fields
def reset_form():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_job_role.delete(0, tk.END)
    entry_qualification.delete(0, tk.END)
    entry_comments.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x400")  # Set window size to mimic the layout in the image

# Form Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Mobile No:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_mobile = tk.Entry(root, width=30)
entry_mobile.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Job Role:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_job_role = tk.Entry(root, width=30)
entry_job_role.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Qualification:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_qualification = tk.Entry(root, width=30)
entry_qualification.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="comments:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_comments = tk.Entry(root, width=30)
entry_comments.grid(row=5, column=1, padx=10, pady=5)

# Buttons for Submit and Cancel
submit_button = tk.Button(root, text="Save", command=submit_data, bg="green", fg="white", width=10)
submit_button.grid(row=6, column=0, padx=10, pady=20, sticky="e")

cancel_button = tk.Button(root, text="Cancel", command=reset_form, bg="red", fg="white", width=10)
cancel_button.grid(row=6, column=1, padx=10, pady=20, sticky="w")

# Start the Tkinter event loop
root.mainloop()
