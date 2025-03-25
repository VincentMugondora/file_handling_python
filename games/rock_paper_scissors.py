# rock paper scissors game
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {
        "player": player_choice, 
        "computer": computer_choice
        }

    return choices

def check_win(player, computer):
    return [player, computer]




# # how random works
# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)
# print(dinner)

number = [1,3,4,6,8,9]
number[3]
print(number)
number[:3]