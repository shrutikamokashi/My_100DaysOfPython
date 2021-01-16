# TODO: Asking Qs
# TODO: Checking the answer
# TODO: checking if we are at end

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.question_list)

    def next_question(self):
        curr_q = self.question_list[self.q_num]
        self.q_num += 1
        answer = input(f"Q{self.q_num}. {curr_q.text} (True/False)?: ")
        self.check_ans(answer, curr_q.answer)

    def check_ans(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong\nCorrect ans is '{correct_answer}'")
        print(f"Your current score is: {self.score}/{self.q_num}")



