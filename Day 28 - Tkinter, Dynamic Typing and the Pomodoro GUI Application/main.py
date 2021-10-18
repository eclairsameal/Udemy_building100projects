from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Lable
lable_title = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
lable_title.grid(row=0, column=1)

lable_check = Label(text="✔", font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
lable_check.grid(row=3, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # 去掉邊框
tomato_img = PhotoImage(file="tomato.png")  # 使用圖片前要先載入
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Button
button_star = Button(text="Start", highlightthickness=0)
button_star.grid(row=2, column=0)
button_reset = Button(text="Reset", highlightthickness=0)
button_reset.grid(row=2, column=2)

window.mainloop()