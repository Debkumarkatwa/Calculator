# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define the style for combobox widget

# Define an event to close the window
def close_win(e):
   win.destroy()
# Add a label widget
# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: close_win(e))

win.mainloop()