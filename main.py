from question_model import Question
from data import new_data
from quiz_brain import QuizBrain

question_bank = []

for question in new_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quizz = QuizBrain(question_bank)

game_on = True

while game_on:
    if quizz.still_has_questions():
        quizz.next_question()
    else:
        print(f"You've completed the quiz.\nYour final score is: {quizz.score}/12")
        game_on = False
