# Number Guessing Game: A game where the user has to guess a randomly generated number
import random

def guessing_game():
    secret_num = random.randint(1, 100)
    print("Guess a number between 1 and 100 or type 1000 to exit")
    guess_chances = 0
    guess_limit = 5
    guess_number = 0

    while guess_chances < guess_limit:
        guess_number = int(input("Guess a number: "))

        if guess_number == 1000:
            print("Exiting the game")
            break
        elif guess_number > secret_num:
            print(f"{guess_number} is greater than the secret number.")
            guess_chances = guess_chances + 1
            print(guess_chances)
        elif guess_number < secret_num:
            print(f"{guess_number} is less than the secret number.")
            guess_chances = guess_chances + 1
            print(guess_chances)
        elif guess_number == secret_num:
            print(f"{guess_number} is correct. You win!! 🎆🎇🎆🎆🎇")
            secret_num = random.randint(1, 100)
            replay = input("Do you want to replay (yes/no)").lower()
            if replay == "yes":
                guess_chances = 0
                print("Starting a new game and you have been given 5 chances!")
            elif replay == "no":
                print("Exiting the game")
                break
            else:
                    print("Dont understand the command enter (yes/no)")
                    replay = input("Do you want to replay (yes/no)").lower()
    else:
        print("You lose!!! 😥😥😭😭")

guessing_game()