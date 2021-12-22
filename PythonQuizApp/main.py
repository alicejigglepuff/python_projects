from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#creating a list of question objects from data
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


#Quizbrain and next_question() method
#create a new quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz. Your final score was {quiz.score}/{len(question_bank)}")
