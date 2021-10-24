from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Label in Canvas
label_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
label_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0)
button_right.grid(row=1, column=0)
img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=1)


window.mainloop()