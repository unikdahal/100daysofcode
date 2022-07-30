# The Quiz Game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:

    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

still_has_question=True
quiz = QuizBrain(question_bank)
while still_has_question:

    quiz.next_question()
    still_has_question=quiz.still_has_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")