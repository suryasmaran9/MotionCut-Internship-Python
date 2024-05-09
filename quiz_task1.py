class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            user_answer = input(question.prompt + "\nYour answer: ")
            if user_answer == str(question.answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        print(f"You got {self.score} out of {len(self.questions)} questions correct.")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Define your questions
questions = [
    Question("What is 2 + 2? ", 4),
    Question("What is 7 * 3? ", 21),
    Question("What is 10 - 5? ", 5),
]

# Create a quiz object
quiz = Quiz(questions)

# Run the quiz
quiz.run_quiz()
