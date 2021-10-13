#import tkinter
from tkinter import *

window = Tk()
window.title("Tkinter Program")
window.minsize(width=500, height=300)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


window.mainloop()