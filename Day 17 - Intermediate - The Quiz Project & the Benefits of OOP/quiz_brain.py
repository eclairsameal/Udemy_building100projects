class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        """
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        """

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}: {current_question.text} (True/False)?:')
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, answer):
        if user_ans.lower() == answer.lower():
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")


