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

# Average Grade Calculations
def calculate_average_grade(df):
    return df['grade'].mean()
# Using SQLite
def calculate_average_grade_sqlite():
    conn = sqlite3.connect('student_grades.db')
    cursor = conn.cursor()

    # using AVG function
    cursor.execute("SELECT AVG(grade) FROM student_data")
    avg_grade = cursor.fetchone()[0]
    conn.close()
    return avg_grade

# Average Attendance
def calculate_average_attendance(df):
    return df['attendance'].mean()
# Using SQLite
def calculate_average_attendance_sqlite():
    conn = sqlite3.connect('student_grades.db')
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(attendance) FROM student_data")
    avg_attendance = cursor.fetchone()[0]
    conn.close()
    return avg_attendance

# Number of Passes
def calculate_num_passes(df):
    #defining passes means >40
    #if pass assign value 1, if fail assign 0
    passes = df['grade'] > 40
    # calculates number of passes
    return passes.sum()
# Using SQLite
def calculate_num_passes_sqlite():
    conn = sqlite3.connect('student_grades.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(ALL) FROM student_data WHERE grade > 40")
    num_passes = cursor.fetchone()[0]
    conn.close()
    return num_passes

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
    labels = ['Fail', 'C', 'B', 'A']
    df['grade_band'] = pd.cut(df['grade'], bins=bounds, labels=labels, right=True)
    # Count how many students fall into each band
    counts = df['grade_band'].value_counts()

    # Reorder to A, B, C, Fail
    ordered = ['A', 'B', 'C', 'Fail']
    return counts.reindex(ordered)
def grade_distribution_sqlite(df):
    conn = sqlite3.connect('student_grades.db')
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT grade_band, COUNT(*) as count
                   FROM (
                       SELECT
                       CASE
                       WHEN grade < 40 THEN 'Fail'
                       WHEN grade < 60 THEN 'C'
                       WHEN grade < 70 THEN 'B'
                       ELSE 'A'
                       END AS grade_band
                       FROM student_data
                       )
                   GROUP BY grade_band
                   """)

    results = cursor.fetchall()
    conn.close()

    # Convert results into a dictionary
    counts = {band: count for band, count in results}

    # Reorder to A, B, C, Fail
    ordered = ['A', 'B', 'C', 'Fail']
    return {band: counts.get(band, 0) for band in ordered}

if __name__ == "__main__":
    df = get_data()
    print("Average grade:", calculate_average_grade(df))
    print("Average attendance:", calculate_average_attendance(df))
    print("No. of passes:", calculate_num_passes(df))
    print("Grade distribution:", grade_distribution(df))