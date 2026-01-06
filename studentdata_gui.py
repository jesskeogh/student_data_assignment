import numpy as np
# Imports tkinter into the
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
# Size of the app
app.geometry('500x500')
#
#app.resizable(False, False)
# Title of the app
app.title("Student Data Menu")
# Text inside the app
ttk.Label(app, text="Menu").grid(column=0, row=0)

# Exit Button
exit_button = ttk.Button(
    app,
    text="Exit",
    command=lambda: app.quit()
)

exit_button.grid(
    column=0,
    row=1,
    padx=10,
    pady=10
)

app.mainloop()
