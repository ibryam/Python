from question_model import Question
from data import question_data
from quiz_brain import QuizBrain, question_number

question_bank = []

for q in question_data:

    question = q["text"]
    answer = q["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): #if quiz still has questions remaining
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")





# print(question_bank)



