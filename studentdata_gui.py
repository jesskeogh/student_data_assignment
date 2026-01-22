# Student data GUI File
import tkinter as tk
from tkinter import ttk
from calculations import (
    calculate_average_grade_sqlite,
    calculate_average_attendance_sqlite,
    calculate_num_passes_sqlite,
    calculate_num_fails_sqlite,
    grade_distribution_sqlite
)
from database_operations import (
    get_data,
    read_csv_data
)
from graphing import (
    plot_grade_distribution,
    plot_grade_against_attendance,
    plot_grade_against_age,
    plot_pass_vs_fail_pie
)

conn = get_data()
df = read_csv_data()

app = tk.Tk()
# Size of the app
app.geometry('500x500')
# Title of the app
app.title("Student Data Menu")
# Text inside the app
ttk.Label(app, text="Menu").grid(column=0, row=0)


# Show average grade
def show_avg_grade():
    avg = calculate_average_grade_sqlite(conn)
    avg_label.config(text=f"Average Grade: {avg:.2f}")


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
avg_label.grid(column=1, row=1, padx=10, pady=10)


# Show average attendance
def show_avg_attendance():
    avg_att = calculate_average_attendance_sqlite(conn)
    avg_att_label.config(text=f"Average Attendance: {avg_att:.2f}")


show_average_attendance = ttk.Button(
    app,
    text="Show average attendance (SQL)",
    command=show_avg_attendance
)
show_average_attendance.grid(
    column=0,
    row=2,
    padx=10,
    pady=10
)
avg_att_label = ttk.Label(app, text="Average attendance will appear here")
avg_att_label.grid(column=1, row=2, padx=10, pady=10)


# Show number of passes
def show_num_of_passes():
    num_pass = calculate_num_passes_sqlite(conn)
    num_pass_label.config(text=f"Number of Passes: {num_pass:}")


show_num_passes = ttk.Button(
    app,
    text="Show number of passes (SQL)",
    command=show_num_of_passes
)
show_num_passes.grid(
    column=0,
    row=3,
    padx=10,
    pady=10
)
num_pass_label = ttk.Label(app, text="Number of Passes will appear here")
num_pass_label.grid(column=1, row=3, padx=10, pady=10)


# Show number of fails
def show_num_of_fails():
    num_fails = calculate_num_fails_sqlite(conn)
    num_fails_label.config(text=f"Number of Fails: {num_fails:}")


show_num_fails = ttk.Button(
    app,
    text="Show number of fails (SQL)",
    command=show_num_of_fails
)
show_num_fails.grid(
    column=0,
    row=4,
    padx=10,
    pady=10
)
num_fails_label = ttk.Label(app, text="Number of Fails will appear here")
num_fails_label.grid(column=1, row=4, padx=10, pady=10)


# Show grade distribution
def show_grade_distribution():
    data = grade_distribution_sqlite(conn)
    # Convert list of tuples into readable text
    formatted = "\n".join([f"{grade}: {count}" for grade, count in data])
    grade_dist_label.config(text=formatted)


show_grade_dist_button = ttk.Button(
    app,
    text="Show Grade Distribution",
    command=show_grade_distribution
)
show_grade_dist_button.grid(
    column=0,
    row=5,
    padx=10,
    pady=10
)

grade_dist_label = ttk.Label(app, text="Grade distribution will appear here")
grade_dist_label.grid(column=1, row=5, padx=10, pady=10)


# Code to show grade attendance
def show_grade_distribution():
    plot_grade_distribution(conn)


show_grade_distribution = ttk.Button(
    app,
    text="Show grade distribution graph",
    command=show_grade_distribution
)
show_grade_distribution.grid(
    column=0,
    row=9,
    padx=10,
    pady=10
)


# Code to show grade vs attendance
def show_grade_against_attendance():
    plot_grade_against_attendance(df)


show_grade_against_attendance = ttk.Button(
    app,
    text="Show grade against attendance graph",
    command=show_grade_against_attendance
)
show_grade_against_attendance.grid(
    column=0,
    row=10,
    padx=10,
    pady=10
)


# Code to show age vs grade
def show_grade_against_age():
    plot_grade_against_age(df)


show_grade_against_age = ttk.Button(
    app,
    text="Show grade against age graph",
    command=show_grade_against_age
)
show_grade_against_age.grid(
    column=0,
    row=11,
    padx=10,
    pady=10
)


def show_passes_vs_fails():
    plot_pass_vs_fail_pie(conn)


show_passes_vs_fails = ttk.Button(
    app,
    text="Show passes vs. fails pie",
    command=show_passes_vs_fails
)
show_passes_vs_fails.grid(
    column=0,
    row=12,
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
    row=100,
    padx=10,
    pady=10
)
app.mainloop()


conn.close()
