# create dataframe from csv file - make function?
# import pandas and SQLite
import pandas as pd
import sqlite3

def create_db():
    df = pd.read_csv('student_grades.csv')
    conn = sqlite3.connect("student_grades.db")
    with conn:
        df.to_sql("student_data", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == '__main__':
    create_db()

#create_db()

#c = conn.cursor()
#for row in c.execute('SELECT * FROM student_data'):
#    print(row)

#import as a function
#def db_connection():
  #  return sqlite3.connect('data/student_grades.db')
