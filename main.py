# this is a test page to ensure this works for my assignment

# Importing required libraries
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
