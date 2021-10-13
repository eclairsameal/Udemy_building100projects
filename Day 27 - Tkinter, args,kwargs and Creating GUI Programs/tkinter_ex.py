#import tkinter
from tkinter import *

window = Tk()
window.title("Tkinter Program")
window.minsize(width=500, height=300)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    #my_label.config(text="Button got clicked")
    my_label.config(text=input.get())
    print("I got clicked")


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()
#print(input.get())



window.mainloop()