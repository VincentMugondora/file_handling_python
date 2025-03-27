import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    while True:
        user_choice = input("Enter your choice (optional: rock, paper or scissors): ").lower()
        if user_choice == computer_choice:
            print("It's a tie!")

        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
            else:
                print("Computer wins!")
                print("Rock crushes scissors!")
                print("Paper disproves scissors!")

        elif user_choice == "paper":

            if computer_choice == "rock":
                print("You win!")
                print("Paper covers rock!")
            else:
                print("Computer wins!")
                print("Paper covers rock!")
                print("Scissors cuts paper!")

        elif user_choice == "quit":
            print("Goodbye!")
            break

rock_paper_scissors()