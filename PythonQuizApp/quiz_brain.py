#    TODO 1. ask the question
#    TODO 2. check if the answer is correct
#    TODO 3. check if we are at the end of the quiz

class QuizBrain:


    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"Your current score is {self.score}/{self.question_number}")