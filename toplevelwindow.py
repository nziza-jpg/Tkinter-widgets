# Import necessary libraries
from tkinter import *

# Setting up main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    # Adding a label widget to Top Window
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()

    top.mainloop()

# Adding a label and button widget to Root (Main) Window
l = Label(root, text = "This is root window")
btn = Button(root, text = "Clixk here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

root.mainloop()