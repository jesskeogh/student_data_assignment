## **Student Data Analysis Application**

This project is a Python application designed to read student grade data, store it in an SQLite database, and provide a simple graphical interface for viewing grade statistics and visualisations.

The system demonstrates:

- Reading and processing CSV data
- Creating and querying an SQLite database
- Displaying results through a Tkinter GUI
- Generating charts using Matplotlib
- Applying basic object‑oriented programming
- Using unit tests to validate functionality

How to Run the Application

To use the program, you must run the application from the studentdata_gui.py file.
This file launches the Tkinter interface and connects all other parts of the project together.

**Steps:**
Make sure all project files are in the same folder

Ensure the CSV file is present so the database can be created

**Run:**

Code
python studentdata_gui.py
The GUI will open, allowing you to:
- View grade distribution
- Calculate average grades
- Display charts
- Interact with the database

Running any other file directly will not launch the full application.


**Project Structure**

database_operations.py – Reads CSV data and creates the SQLite database

calculations.py – Contains SQL‑based grade calculations

studentdata_gui.py – Main GUI application (must be run first)

plotting.py – Generates charts for grade distribution

tests/ – Unit tests for database, calculations, and GUI behaviour

**Requirements**
- Python 3
- Tkinter
- SQLite (built into Python)
- Pandas
- Matplotlib

Install missing packages with:

Code
pip install pandas matplotlib

Notes
The database is automatically created from the CSV file if it does not already exist

The GUI updates dynamically based on database queries

Tests are included to demonstrate functionality and error handling
