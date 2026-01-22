"""
How to put a graph inside a Tkinter window
https://www.geeksforgeeks.org/python/how-to-embed-matplotlib-charts-in-tkinter-gui/

"""
import numpy as np
# Imports tkinter into the
import tkinter as tk
from tkinter import ttk
from calculations import calculate_average_grade_sqlite
from database_operations import get_data, read_csv_data
from graphing import plot_grade_distribution, plot_grade_against_attendance
import matplotlib.pyplot as plt

conn = get_data()
df = read_csv_data()


app = tk.Tk()
# Size of the app
app.geometry('500x500')
#
#app.resizable(False, False)
# Title of the app
app.title("Student Data Menu")
# Text inside the app
ttk.Label(app, text="Menu").grid(column=0, row=0)

def show_avg_grade():
    avg = calculate_average_grade_sqlite(conn)
    avg_label.config(text=f"Average Grade: {avg}")

# Show average grade
show_average_grade = ttk.Button(
    app,
    text="Show average grade (SQL)",
    command=show_avg_grade
)
show_average_grade.grid(
    column=0,
    row=1,
    padx=10,
    pady=10
)

avg_label = ttk.Label(app, text="Average grade will appear here")
avg_label.grid(column=0, row=2, padx=10, pady=10)

show_grade_against_attendance = ttk.Button(
    app,
    text="Show grade against attendance",
    command=plot_grade_against_attendance(df)
)
show_grade_against_attendance.grid(
    column=1,
    row=2,
    padx=10,
    pady=10
)

# Exit Button
exit_button = ttk.Button(
    app,
    text="Exit",
    command=lambda: app.quit()
)
exit_button.grid(
    column=0,
    row=10,
    padx=10,
    pady=10
)
app.mainloop()


conn.close()