from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
from data_op import question_data

question_bank = []
for q in question_data["results"]:
    #new_question = Question(q["text"], q["answer"])
    new_question = Question(q["question"], q["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")