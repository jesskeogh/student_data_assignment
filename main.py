# this is a test page to ensure this works for my assignment

import numpy as np

#quick_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
#print(quick_array)

import studentdata_gui as tk

from studentdata_gui import ttk
"""
win = tk.Tk()
win.geometry('500x500')
win.title("Python GUI Time")
ttk.Label(win, text="Python GUI Time").grid(column=0, row=0)
win.mainloop()
"""

# Import required libraries
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect(r"./data/student_grades.db")

# Load CSV data into Pandas DataFrame
stud_data = pd.read_csv('data/student_grades.csv')
# Write the data to a sqlite table
stud_data.to_sql('student', conn, if_exists='replace', index=False)

# Create a cursor object
cur = conn.cursor()
# Fetch and display result
for row in cur.execute('SELECT * FROM student'):
    print(row)
# Close connection to SQLite database
conn.close()


