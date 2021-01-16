from question_model import Question
# from data import question_data
from data_n import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_q = Question(q["question"], q["correct_answer"])
    # for key in q:
    #     new_q = Question(key, q[key])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou have completed the quiz.")
print(f"\nYour final score is {quiz.score}/{quiz.q_num}")
