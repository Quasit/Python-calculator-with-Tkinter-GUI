import tkinter as tk
#from tkinter import ttk
from functions import click
import globals as gl

# Main file, which builds application window, and it's content like labels and buttons

# Function which gets keyboard input and calls 'click' function
def onKeyPress(event):
    click(label, str(event.keysym))

def copy_to_clipboard(event):
    root.clipboard_append(gl.output)

# Initialization of global variable
gl.init()

# Application root configuration
root = tk.Tk()
root.geometry("380x460")
root.resizable(0, 0)
root.configure(bg=gl.default_color)
root.option_add("*font", "Verdana 16 bold")

# Frame configuration
frame = tk.Frame(root, background=gl.default_color)
frame.configure(bg=gl.default_color)
frame.columnconfigure(0, pad=3)
frame.columnconfigure(1, pad=3)
frame.columnconfigure(2, pad=3)
frame.columnconfigure(3, pad=3)

frame.rowconfigure(0, pad=3)
frame.rowconfigure(1, pad=3)
frame.rowconfigure(2, pad=3)
frame.rowconfigure(3, pad=3)
frame.rowconfigure(4, pad=3)
frame.rowconfigure(5, pad=3,)

# Buttons and labels configuration
# First row
label = tk.Label(frame, text=gl.output, fg="white", width=20, heigh=3, background=gl.colors["grey"], font=(15), anchor="e")
label.grid(row=0, columnspan=4, sticky=tk.W+tk.E)
# Second row
ac = tk.Button(frame, text="AC", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, 'AC')])
ac.grid(row=1, column=0)
backspace = tk.Button(frame, text="⌫", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '⌫')])
backspace.grid(row=1, column=1)
percentage = tk.Button(frame, text="%", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '%')])
percentage.grid(row=1, column=2)
divide = tk.Button(frame, text="÷", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '÷')])
divide.grid(row=1, column=3)
seven = tk.Button(frame, text="7", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 7)])
seven.grid(row=2, column=0)
eight = tk.Button(frame, text="8", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 8)])
eight.grid(row=2, column=1)
nine = tk.Button(frame, text="9", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 9)])
nine.grid(row=2, column=2)
multiplication = tk.Button(frame, text="×", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda: [click(label, '×')])
multiplication.grid(row=2, column=3)

# Third row
four = tk.Button(frame, text="4", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 4)])
four.grid(row=3, column=0)
five = tk.Button(frame, text="5", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 5)])
five.grid(row=3, column=1)
six = tk.Button(frame, text="6", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 6)])
six.grid(row=3, column=2)
minus = tk.Button(frame, text="-", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '-')])
minus.grid(row=3, column=3)

# Fourth row
one = tk.Button(frame, text="1", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 1)])
one.grid(row=4, column=0)
two = tk.Button(frame, text="2", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 2)])
two.grid(row=4, column=1)
three = tk.Button(frame, text="3", width=5, heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 3)])
three.grid(row=4, column=2)
plus = tk.Button(frame, text="+", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '+')])
plus.grid(row=4, column=3)

# Fifth row
zero = tk.Button(frame, text="0", heigh=2, background=gl.colors["orange"], relief="flat", command=lambda:[click(label, 0)])
zero.grid(row=5, column=0, columnspan=2, sticky="we", padx=(1,2))
dot = tk.Button(frame, text=".", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '.')])
dot.grid(row=5, column=2)
equal = tk.Button(frame, text="=", width=5, heigh=2, background=gl.colors["blue"], relief="flat", command=lambda:[click(label, '=')])
equal.grid(row=5, column=3)

frame.pack()

# Getting keyboard input
root.bind('<Key>', onKeyPress)
root.bind('<Return>', lambda solve: click(label, '=')) # Since event.keysym == 'Return' wasn't working, had to make separate bind for it
root.bind('<Control-c>', copy_to_clipboard)

# Start of application window
root.mainloop()