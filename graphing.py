# this is where I do the graphing for my assignment basics

# this is where I do the graphing for my assignment basics

# imports matplotlib and functions from
import matplotlib.pyplot as plt
from calculations import get_data, grade_distribution

def plot_grade_distribution():
    df = get_data()
    counts = grade_distribution(df)

    # order by grade name
    order = ['A', 'B', 'C', 'Fail']
    counts = counts.reindex(order)

    # Bar chart
    counts.plot(kind='bar', color=['green','orange','blue','red'])
    plt.title("Grade Distribution")
    plt.xlabel("Grade Band")
    plt.ylabel("Number of Students")
    plt.show()

def plot_grade_distribution_pie():
    df = get_data()
    counts = grade_distribution(df)
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Grade Distribution")
    plt.ylabel("")  # hide y-label
    plt.show()

import sqlite3
import pandas as pd
import numpy as np

def grade_against_attendance():
    conn = sqlite3.connect('student_grades.db')
    df = pd.read_sql_query("SELECT grade, attendance FROM student_data", conn)
    conn.close()
    return df

# load data
df = grade_against_attendance()

# get X and Y values
x = df['attendance']
y = df['grade']

# create scatter graph
plt.scatter(x, y, alpha=0.5) # alpha is the density of the data points
plt.xlabel("attendance (%)")
plt.ylabel("Grade")
plt.title("Correlation between Attendance and Grade")

# Add trendline
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')

plt.show()

if __name__ == "__main__":
    plot_grade_distribution()
    plot_grade_distribution_pie()