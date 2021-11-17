from tkinter import *


def mile_to_km():
    ans_km = float(input_miles.get()) * 1.609344
    label_ans_km.config(text=f"{ans_km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

input_miles = Entry()
input_miles.grid(row=0, column=1)

label_miles = Label(text="Miles", font=("Arial", 16))
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to", font=("Arial", 16))
label_equal.grid(row=1, column=0)

label_ans_km = Label(text="0", font=("Arial", 16))
label_ans_km.grid(row=1, column=1)

label_km = Label(text="Km", font=("Arial", 16))
label_km.grid(row=1, column=2)

button = Button(text="Calculate", command=mile_to_km)
button.grid(row=2, column=1)

window.mainloop()