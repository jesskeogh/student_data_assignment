# create dataframe from csv file - make function?
import pandas as pd
df = pd.read_csv('student_grades.csv')

# import SQLite
import sqlite3
conn = sqlite3.connect(r"student_grades.db")

#import as a function
#def db_connection():
  #  return sqlite3.connect('data/student_grades.db')

def create_db():
    with conn:
        df.to_sql("student_data", conn, if_exists="replace", index=False)

create_db()

c = conn.cursor()
for row in c.execute('SELECT * FROM student_data'):
    print(row)