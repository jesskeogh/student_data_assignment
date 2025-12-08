#
# def get_number_of_As(df):
#     return len(df[df["grade"] >= 70])
#
# #get number of As from sql (grade >= 70)
# def get_number_of_As_sql(conn):
#     cur = conn.cursor()
#     return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade >= 70").fetchone()[0]
"""
from create_db import create_db

create_db()

c = conn.cursor()
for row in c.execute('SELECT * FROM student_data'):
    print(row)
"""

import sqlite3
import pandas as pd

def get_data():
    conn = sqlite3.connect('student_grades.db')
    df = pd.read_sql_query(
        'SELECT * FROM student_data', conn )
    conn.close()
    return df

# go back and redo these functions using sqlite

def calculate_average_grade(df):
    return df['grade'].mean()

def calculate_average_attendance(df):
    return df['attendance'].mean()

def calculate_num_passes(df):
    #defining passes means >40
    #if pass assign value 1, if fail assign 0
    passes = df['grade'] > 40
    # calculates number of passes
    return passes.sum()

#Calculates the number of grades in each boundary
# Easier/More efficient to combine the functions into one to save...
"""
def calculate_no_a_grades(df):
    a_grades = df['grade'] > 70
    return a_grades.sum()

def calculate_no_b_grades(df):
    b_grades = (df['grade'] <= 70) & (df['grade'] > 60)
    return b_grades.sum()
"""

def grade_distribution(df):
    bounds = [0, 40, 60, 70, 100]  # boundaries
    labels = ['A', 'B', 'C', 'Fail']
    df['grade_band'] = pd.cut(df['grade'], bins=bounds, labels=labels, right=True)
    return df['grade_band'].value_counts()

if __name__ == "__main__":
    df = get_data()
    print("Average grade:", calculate_average_grade(df))
    print("Average attendance:", calculate_average_attendance(df))
    print("No. of passes:", calculate_num_passes(df))
    print("Grade distribution:", grade_distribution(df))