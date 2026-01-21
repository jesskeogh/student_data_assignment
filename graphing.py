# this is where I do the graphing for my assignment basics
# this is where I do the graphing for my assignment basics

# imports matplotlib and functions from
import matplotlib.pyplot as plt
from calculations import grade_distribution_sqlite
from database_operations import get_data, read_csv_data

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
    counts.plot(kind='bar', color=['green','orange','blue','red'])
    plt.title("Grade Distribution")
    plt.xlabel("Grade Band")
    plt.ylabel("Number of Students")
    plt.show()

# Grade distribution shown on a pie chart
# def plot_grade_distribution_pie():
#     df = get_data()
#     counts = grade_distribution(df)
#     counts.plot(kind='pie', autopct='%1.1f%%')
#     plt.title("Grade Distribution")
#     plt.ylabel("")  # hide y-label
#     plt.show()

import sqlite3
import pandas as pd
import numpy as np

def plot_grade_against_attendance(df):
    plt.clf()
    # get X and Y values
    x = df['attendance']
    y = df['grade']

    # create scatter graph
    plt.scatter(x, y, alpha=0.5) # alpha is the density of the data points

    plt.xlabel("attendance (%)")
    plt.ylabel("Grade")
    plt.title("Correlation between Attendance and Grade")

    # Add trendline
    coeff = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coeff)
    plt.plot(x, polynomial(x), color='red')
    plt.show()

# if __name__ == "__main__":
    # conn = get_data()
    # df = read_csv_data()
    # plot_grade_distribution(conn)
    # #plot_grade_distribution_pie()
    # plot_grade_against_attendance(df)
    # conn.close()