from  tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # 先宣告傳入的資料是什麼型態，避免犯錯
        self.quit = quiz_brain
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
            width=280,  # 設定寬，文字超出會換行
            text="question_text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # canvas 的 padding 在這設定

        # Button
        true_img = PhotoImage(file="images/true.png")  # 使用圖片前要先載入
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")  # 使用圖片前要先載入
        self.button_false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)
        
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # 背景變回白色
        q_text = self.quit.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        # is_right = self.quit.check_answer("True")
        # self.give_feedback(is_right)
        self.give_feedback(self.quit.check_answer("True"))
        
    def false_pressed(self):
        # is_right = self.quit.check_answer("False")
        self.give_feedback(self.quit.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  # 1秒後執行 self.get_next_question
        
        