from  tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,  bg=THEME_COLOR)

        # Label
        self.label_score = Label(text="Score:0", font=("Arial", 15, "bold"),  bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="question_text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # canvas 的 padding 在這設定

        # Button
        true_img = PhotoImage(file="images/true.png")  # 使用圖片前要先載入
        self.button_true = Button(image=true_img, highlightthickness=0)
        self.button_true.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")  # 使用圖片前要先載入
        self.button_false = Button(image=false_img, highlightthickness=0)
        self.button_false.grid(row=2, column=1)


        self.window.mainloop()


