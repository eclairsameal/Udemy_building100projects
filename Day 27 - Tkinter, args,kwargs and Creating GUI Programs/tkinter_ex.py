#import tkinter
from tkinter import *

def button_clicked():
    #my_label.config(text="Button got clicked")
    my_label.config(text=input.get())
    print("I got clicked")


window = Tk()
window.title("Tkinter Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
#my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New button")
button2.grid(column=2, row=0)

# Entry
input = Entry()
input.grid(column=3, row=3)
#print(input.get())



window.mainloop()