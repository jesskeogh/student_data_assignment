# Graphing File
import matplotlib.pyplot as plt
from calculations import (
    grade_distribution_sqlite,
    calculate_num_passes_sqlite,
    calculate_num_fails_sqlite
)
from database_operations import get_data, read_csv_data
import sqlite3
import pandas as pd
import numpy as np


# Graph made using SQL
def plot_grade_distribution(conn):
    plt.clf()
    # conn = get_data()
    counts = grade_distribution_sqlite(conn)

    # Convert list of tuples → Series
    counts = pd.Series(dict(counts))

    # order by grade name
    order = ['A', 'B', 'C', 'Fail']
    counts = counts.reindex(order)

    # Bar chart
    counts.plot(kind='bar', color=['green', 'orange', 'blue', 'red'])
    plt.title("Grade Distribution")
    plt.xlabel("Grade Band")
    plt.ylabel("Number of Students")
    plt.show()


# Passes vs Fails shown on a pie chart
def plot_pass_vs_fail_pie(conn):
    passes = calculate_num_passes_sqlite(conn)
    fails = calculate_num_fails_sqlite(conn)

    labels = ['Passes', 'Fails']
    sizes = [passes, fails]
    colors = ['green', 'red']

    plt.figure(figsize=(5, 5))
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Pass vs Fail Distribution")
    plt.axis('equal')
    plt.show()


def plot_grade_against_attendance(df):
    plt.clf()
    # get X and Y values
    x = df['attendance']
    y = df['grade']

    # create scatter graph
    plt.scatter(x, y, alpha=0.5)  # alpha is the density of the data points

    plt.xlabel("attendance (%)")
    plt.ylabel("Grade")
    plt.title("Correlation between Attendance and Grade")

    # Add trendline
    coeff = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coeff)
    plt.plot(x, polynomial(x), color='red')
    plt.show()


def plot_grade_against_age(df):
    plt.clf()
    x = df['age']
    y = df['grade']

    # create scatter graph
    plt.scatter(x, y, alpha=0.5)
    plt.xlabel("age (years)")
    plt.ylabel("Grade")
    plt.title("Correlation between Age and Grade")

    # Add trendline
    coeff = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coeff)
    plt.plot(x, polynomial(x), color='red')
    plt.show()


"""I have commented this out as this was the code
I used to test that the the graphs run"""
# if __name__ == "__main__":
# conn = get_data()
# df = read_csv_data()
# plot_grade_distribution(conn)
# #plot_grade_distribution_pie()
# plot_grade_against_attendance(df)
# plot_pass_vs_fail_pie()
# conn.close()
