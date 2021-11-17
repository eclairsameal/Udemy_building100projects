from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # 保存亂數出來的單字
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# print(to_learn)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # 停止計時器
    current_card = random.choice(to_learn)
    canvas.itemconfig(label_title, text="French", fill="Black")
    canvas.itemconfig(label_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_background, image=img_front) # 要翻回白色
    flip_timer = window.after(3000, flip_card)  # 重新定時計時器

def flip_card():
    global current_card
    canvas.itemconfig(label_title, text="English", fill="white")
    canvas.itemconfig(label_word, text=current_card["English"], fill="white")
    # img_back = PhotoImage(file="images/card_back.png")  xxx
    canvas.itemconfig(card_background, image=img_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card) # 每 3 秒將卡片翻面

# Canvas
canvas = Canvas(width=800, height=526)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")  # 在function外才不會消失
card_background = canvas.create_image(400, 263, image=img_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Label in Canvas
label_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
label_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=0)
img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=1)

next_card()

window.mainloop()