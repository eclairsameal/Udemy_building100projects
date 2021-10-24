from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
# print(data)
to_learn = data.to_dict(orient="records")
print(to_learn)


def next_card():
    current = random.choice(to_learn)
    canvas.itemconfig(label_title, text="French")
    canvas.itemconfig(label_word, text=current["French"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Label in Canvas
label_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
label_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=0)
img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=1)

next_card()

window.mainloop()