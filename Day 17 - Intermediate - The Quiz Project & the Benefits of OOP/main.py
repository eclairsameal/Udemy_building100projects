from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_bank.append(new_question)

quit = QuizBrain(question_bank)
while quit.still_has_question():
    quit.next_question()