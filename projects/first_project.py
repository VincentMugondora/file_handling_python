# create a quiz game where a player can keep track of their score
# and see their score at the end of the game
import random

def quiz_game():
    score = 0
    print("Welcome to the quiz game!")
    questions = [
        "What is the capital of France?",
        "Which data type is immutable in Python?",
        "Who developed the theory of relativity?",
        "What does HTML stand for?",
        "Which planet is known as the Red Planet?",
        "What is the square root of 64?",
        "Who painted the Mona Lisa?",
        "Which programming language is known for web development?",
        "How many continents are there on Earth?",
        "What is the boiling point of water in Celsius?"
    ]
    
    answers = [
        "Paris",
        "Tuple",
        "Albert Einstein",
        "Hyper Text Markup Language",
        "Mars",
        "8",
        "Leonardo da Vinci",
        "JavaScript",
        "7",
        "100°C"
    ]


   
    for question in questions:
        questions.index(question)
        answer = input(question + " ")

        if answer.lower() == answers[questions.index(question)].lower():
            print("Correct!")
            score += 1
        elif answer.lower() == "quit":
            print(f"Your score is {score} and we are exiting the game")
            break
        else:
            print("Incorrect!")

    print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct!")

quiz_game()