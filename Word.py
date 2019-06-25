import math

class Word:
    def __init__(self, question, answer, file):
        self.question = question
        self.answer = answer
        self.file = file + '.txt'
        print('class created')
        with open(self.file, "a") as f:
            f.write(self.question + " / ")
            f.write(self.answer)



    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def calculate_m(self, time):
        k = 537
        m = k/math.sqrt(time)
        return m

    def calculate_time(self):
        for i in range(0, 336):
            pass


