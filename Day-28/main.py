from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_fimer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lable_title.config(text="Timer")
    lable_check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_timer():
    global reps
    reps += 1
    count_down_time = 0
    if reps == 8:
        count_down_time = LONG_BREAK_MIN
        lable_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down_time = SHORT_BREAK_MIN
        lable_title.config(text="Break", fg=PINK)
    else:
        count_down_time = WORK_MIN
        lable_title.config(text="Work", fg=GREEN)
    count_down(count_down_time * 60)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # print(count)
    min, sec = divmod(count, 60)
    canvas.itemconfig(timer_text, text="{:0>2d}:{:0>2d}".format(min, sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        star_timer()  # 重啟計時器
        marks = ""
        work_sessions = math.floor((reps/2))
        for _ in range(work_sessions):
            marks += "✔"
        lable_check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Lable
lable_title = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
lable_title.grid(row=0, column=1)

lable_check = Label(font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
lable_check.grid(row=3, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # 去掉邊框
tomato_img = PhotoImage(file="tomato.png")  # 使用圖片前要先載入
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # 變數化，方便修改
canvas.grid(row=1, column=1)

# Button
button_star = Button(text="Start", highlightthickness=0, command=star_timer)  # call star_timer
button_star.grid(row=2, column=0)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_fimer)
button_reset.grid(row=2, column=2)




window.mainloop()